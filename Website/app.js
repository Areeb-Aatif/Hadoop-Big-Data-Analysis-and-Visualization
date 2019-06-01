new Vue({
  el:'#vue-app',
  data:{
    active:false,
    selected1: null,
    selected2: null,
    top: 10,
    options1: [
      { value: null, text: 'Select Data Source'},
      { value: 'a', text: 'Twitter'},
      { value: 'b', text: 'New York Times'},
      { value: 'c', text: 'Common Crawl'}
    ],
    options2: [
      { value: null, text: 'Select Sub Topic'},
      { value: 'a', text: 'Fraud | Scam'},
      { value: 'b', text: 'Murder'},
      { value: 'c', text: 'Mass Shooting'},
      { value: 'd', text: 'Theft | Robbery'},
      { value: 'e', text: 'All'}
    ],
    heading2: {
      top: '5%'
    },
    mainDiv: {
      display: 'flex',
      height: '100%'
    },
    sidebar: {
      flex: '20%',
      backgroundColor: '#BFBABA'
    },
    graph: {
      flex: '80%'
    },
    select1: {
      position: 'absolute',
      top: '50%'
    },
    select2: {
      top: '60%'
    }
  },
  methods:{
    drawGraph: function(x, id) {
      document.getElementById(id).innerHTML="";
      if((this.selected1 == null) || (this.selected2 == null)){
        return;
      }
      var top = this.top;
      if ((this.selected1 == 'b') && (this.selected2 == 'a')){
        if (x == 'wc'){
          filename = 'data/NY-Output/SubTopic1/part2'
        }
        if (x == 'wcc'){
          filename = 'data/NY-Output/SubTopic1/part3'
        }
      }else if ((this.selected1 == 'b') && (this.selected2 == 'b')){
        if (x == 'wc'){
          filename = 'data/NY-Output/SubTopic2/part2'
        }
        if (x == 'wcc'){
          filename = 'data/NY-Output/SubTopic2/part3'
        }
      }else if ((this.selected1 == 'b') && (this.selected2 == 'c')){
        if (x == 'wc'){
          filename = 'data/NY-Output/SubTopic3/part2'
        }
        if (x == 'wcc'){
          filename = 'data/NY-Output/SubTopic3/part3'
        }
      }else if ((this.selected1 == 'b') && (this.selected2 == 'd')){
        if (x == 'wc'){
          filename = 'data/NY-Output/SubTopic4/part2'
        }
        if (x == 'wcc'){
          filename = 'data/NY-Output/SubTopic4/part3'
        }
      }else if ((this.selected1 == 'b') && (this.selected2 == 'e')){
          if (x == 'wc'){
            filename = 'data/NY-Output/All/part2'
          }
          if (x == 'wcc'){
            filename = 'data/NY-Output/All/part3'
          }
      }else if ((this.selected1 == 'c') && (this.selected2 == 'a')){
        if (x == 'wc'){
          filename = 'data/CC-Output/SubTopic1/part2'
        }
        if (x == 'wcc'){
          filename = 'data/CC-Output/SubTopic1/part3'
        }
      }else if ((this.selected1 == 'c') && (this.selected2 == 'b')){
        if (x == 'wc'){
          filename = 'data/CC-Output/SubTopic2/part2'
        }
        if (x == 'wcc'){
          filename = 'data/CC-Output/SubTopic2/part3'
        }
      }else if ((this.selected1 == 'c') && (this.selected2 == 'c')){
        if (x == 'wc'){
          filename = 'data/CC-Output/SubTopic3/part2'
        }
        if (x == 'wcc'){
          filename = 'data/CC-Output/SubTopic3/part3'
        }
      }else if ((this.selected1 == 'c') && (this.selected2 == 'd')){
        if (x == 'wc'){
          filename = 'data/CC-Output/SubTopic4/part2'
        }
        if (x == 'wcc'){
          filename = 'data/CC-Output/SubTopic4/part3'
        }
      }else if ((this.selected1 == 'c') && (this.selected2 == 'e')){
        if (x == 'wc'){
          filename = 'data/CC-Output/All/part2'
        }
        if (x == 'wcc'){
          filename = 'data/CC-Output/All/part3'
        }
      }else if ((this.selected1 == 'a') && (this.selected2 == 'a')){
        if (x == 'wc'){
          filename = 'data/Twitter-Output/SubTopic1/part2'
        }
        if (x == 'wcc'){
          filename = 'data/Twitter-Output/SubTopic1/part3'
        }
      }else if ((this.selected1 == 'a') && (this.selected2 == 'b')){
        if (x == 'wc'){
          filename = 'data/Twitter-Output/SubTopic2/part2'
        }
        if (x == 'wcc'){
          filename = 'data/Twitter-Output/SubTopic2/part3'
        }
      }else if ((this.selected1 == 'a') && (this.selected2 == 'c')){
        if (x == 'wc'){
          filename = 'data/Twitter-Output/SubTopic3/part2'
        }
        if (x == 'wcc'){
          filename = 'data/Twitter-Output/SubTopic3/part3'
        }
      }else if ((this.selected1 == 'a') && (this.selected2 == 'd')){
        if (x == 'wc'){
          filename = 'data/Twitter-Output/SubTopic4/part2'
        }
        if (x == 'wcc'){
          filename = 'data/Twitter-Output/SubTopic4/part3'
        }
      }else if ((this.selected1 == 'a') && (this.selected2 == 'e')){
        if (x == 'wc'){
          filename = 'data/Twitter-Output/All/part2'
        }
        if (x == 'wcc'){
          filename = 'data/Twitter-Output/All/part3'
        }
      }
      jQuery.get(filename, function(data) {
        var lines = data.split("\n");
        var input = [];
        for (i=1; i<lines.length; i++) {
          words = lines[i].split("\t");
          var dict = new Object();
          dict["text"] = words[0];
          dict["size"] = parseInt(words[1], 10);
          input[i-1] = dict;
        }
        input.sort(function(first, second){
          return second.size - first.size;
        });
        console.log([input]);
        console.log(top);
        output = input.slice(0, top);
        console.log([output]);
        d3.wordcloud()
          .size([1000, 450])
          .selector('#'+id)
          .words(output)
          .start();
      });
    }
  }
})
