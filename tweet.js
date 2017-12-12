'use stric'

const mongoose = require('./db');
const Schema = mongoose.Schema;
// database connection
let TweetSchema = new Schema({
    text: {
        type: String,
        require: true,
        maxlength: 255
    },
    fullResponse: {
        type: Object
    }
});

module.exports = mongoose.model('Tweet', TweetSchema);