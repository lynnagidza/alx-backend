import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import chai from 'chai';

const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('Jobs', queue)).to.throw(Error, 'Jobs is not an array');
  });
});
