const Twitter = require('twitter');
const credentials = require('./credentials');
const tweet = require('./tweet');
const mongoose = require("mongoose");

// Connection URL
const url = 'mongodb://localhost:27017/distributedComputing';

const client = new Twitter({
    consumer_key: credentials.keys.api_key,
    consumer_secret: credentials.keys.api_secret,
    access_token_key: credentials.keys.access_token_key,
    access_token_secret: credentials.keys.access_token_secret
  });


  let stream = client.stream('statuses/filter', {locations: '-122.995004, 32.323198, -67.799695, 49.893813'});
  stream.on('data', (event) => {
    console.log(event && event.text );
    const tweetObject = new tweet( {
        text: event.text,
        fullResponse: event
    });

    tweetObject.save();
  });
   
  stream.on('error', (error) => {
    throw error;
  });
