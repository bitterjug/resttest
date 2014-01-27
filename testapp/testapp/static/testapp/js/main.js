(function($){

var Term = Backbone.Model.extend({
    defaults: {
        id: 0,
        name: 'default-tag',
        taxonomy: ''
    }
});

var Terms = Backbone.Collection.extend({ model: Term });

var MyView = Backbone.View.extend({
    el: $('#content'),

    initialize: function(){
        _.bindAll(this, 'render', 'addTag');
        this.tags = new Terms();
        this.tags.fetch({ url: '/terms/'});
        this.tags.bind('add', this.addTag);
        this.render();
    },

    render: function(){
        var self = this;
        $(this.el).html("<h2>Tags:</h2>");
        $(this.el).append("<ul></ul>");
        _(this.tags.models).each(function(item){ 
            self.addTag(item);
        }, this);
    },

    addTag: function(tag) {
        $('ul', this.el).append(
            "<li>" + tag.get('name') + "</li>"
        );
    }

});

var myview = new MyView();


})(jQuery);
