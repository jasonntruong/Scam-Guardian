var http = require('http');
var express = require('express');
var path = require('path');

var app = express();

app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/main.html');
});

app.get('/browse.html', (req, res) => {
  res.sendFile(__dirname + '/browse.html');
});

app.get('/steps.html', (req, res) => {
    res.sendFile(__dirname + '/steps.html');
  });

app.get('/reviews.html', (req, res) => {
    res.sendFile(__dirname + '/reviews.html');
});

app.get('/caught.html', (req, res) => {
  res.sendFile(__dirname + '/caughtUser.html');
});

const server = app.listen(8080, () => {
  console.log('Example app listening at http://localhost:8080');
});