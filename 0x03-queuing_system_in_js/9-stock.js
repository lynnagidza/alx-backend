const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id){
    return listProducts.find((product) => product.itemId === id);
};

app.use(express.json());

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

function reserveStockById(itemId, stock){
    return setAsync(itemId, stock);
}

async function getCurrentReservedStockById(itemId){
    const reservedStock = await getAsync(itemId);
    return reservedStock;
}

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentReservedStock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    if (currentReservedStock >= item.stock) {
        res.status(403).json({ status: 'Not enough stock available', itemId });
        return;
    }
    await reserveStockById(itemId, currentReservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
