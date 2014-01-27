(function($){


var MyView = Backbone.View.extend({
    el: $('#content'),

    initialize: function(){
        _.bindAll(this, 'render');
        this.render();
    },

    render: function(){
        $(this.el).html("<h2>From the script</h2>");
    }
});

var myview = new MyView();


})(jQuery);
