const Twitter = require('twitter');
const credentials = require('./credentials');
const tweet = require('./tweet');
const mongoose = require("mongoose"); //declare mongoose variable since we will need later on to use a schema.

// Connection URL
const url = 'mongodb://localhost:27017/distributedComputing';

//use the credentials to access the twitter API
const client = new Twitter({
    consumer_key: credentials.keys.api_key,
    consumer_secret: credentials.keys.api_secret,
    access_token_key: credentials.keys.access_token_key,
    access_token_secret: credentials.keys.access_token_secret
  });


//filter the tweets based on the coordinates that were given for the location
  let stream = client.stream('statuses/filter', {locations: '-122.995004, 32.323198, -67.799695, 49.893813'});
  stream.on('data', (event) => {
    console.log(event && event.text );
    //the schema for the tweets (text:response)
    const tweetObject = new tweet( {
        text: event.text,
        fullResponse: event
    });
    //save the tweet
    tweetObject.save();
  });
   //in case of an error, we show the error message
  stream.on('error', (error) => {
    throw error;
  });
