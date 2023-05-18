const express = require('express');
const { validate, Joi } = require("express-validation");
const ytdl = require('ytdl-core');
const cors = require('cors');


app = express();
app.use(cors());


app.get('/download', (req, res) => {

    const url = req.query.url;
    const quality = req.query.quality;
    const format = req.query.format;

    video = ytdl(url, {
        format: format,
        quality: quality
    }).pipe(res);
});


const port = 4000;

const start = () => {
    app.listen(port, () => {
        console.log(`Server Started on port ${port}`);
    });
};

start();