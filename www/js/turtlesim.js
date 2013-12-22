var TurtleSim = (function() {

  var TurtleSim = function(options) {
    var that = this;
    options = options || {};
    this.ros     = options.ros;
    this.context = options.context;
    this.turtle  = null;
		
  };

  TurtleSim.prototype.spawnTurtle = function(name) {
    var that = this;
    var initialPose = {
      x : that.context.canvas.width / 2
    , y : that.context.canvas.height / 2
    };

    that.turtle = new Turtle({
      name    : name,
      ros     : that.ros,
      pose    : initialPose,
      context : that.context
    });

  };

  TurtleSim.prototype.draw = function() {
    this.context.fillStyle = "BLUE"
    this.context.fillRect(0, 0, this.context.canvas.width, this.context.canvas.height);
    this.turtle.draw();
  };

  return TurtleSim;
}());

