const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create Schema
const Likeschema = new Schema({
  phone: {
    type: String, 
    required: true 
  },
  car: {
	type: String,
	required: true
  },
  date: {
    type: Date,
    default: Date.now
  },

});

module.exports = User = mongoose.model('likes', Likeschema);
