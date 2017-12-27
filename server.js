const fs = require('fs');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());

app.set('views', __dirname + '/views');
app.use('/app', express.static(__dirname + '/app/'));
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);
app.get('/', (req, res) =>{
    res.render('Tweets.ejs')
});

app.post('/data', (req,res) => {
    const search = req.body.type;
    const lines = fs.readFileSync(`${search}.txt`).toString().split("\n");
    const top_words = lines.map(l => {
        if (l){
            const [key, value] = l.split('\t');
            return { [key]: value}
        }
    })
    res.send(top_words)
})

app.listen(3000, function() {
    console.log('App listening on port 3000!');
});

