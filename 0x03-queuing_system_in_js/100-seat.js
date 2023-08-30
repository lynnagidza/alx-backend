const redis = require('redis');
const kue = require('kue');
const express = require('express');
const { promisify } = require('util');

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

setAsync('available_seats', 50);
let reservationEnabled = true;

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.use(express.json());

app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: availableSeats });
});

function reserveSeat(number){
    return setAsync('available_seats', number);
}

async function getCurrentAvailableSeats(){
    const availableSeats = await getAsync('available_seats');
    return parseInt(availableSeats);
}

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ "status": "Reservation are blocked" });
        return;
    }
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats === 0) {
        res.json({ "status": "Reservation are blocked" });
        return;
    }
    const job = queue.create('reserve_seat', {}).save((err) => {
        if (!err) {
            res.json({ "status": "Reservation in process" });
        } else {
            res.json({ "status": "Reservation failed" });
        }
    });
    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', async (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();
        if (availableSeats === 0) {
            reservationEnabled = false;
        } else if (availableSeats < 0) {
            done(Error('Not enough seats available'));
        } else {
            await reserveSeat(availableSeats - 1);
        }
        done();
    });
    res.json({ "status": "Queue processing" });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
