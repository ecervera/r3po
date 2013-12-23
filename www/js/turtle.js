var Turtle = (function() {

  var Turtle = function(options) {
    var that = this;
    options = options || {};
    that.ros     = options.ros;
    that.name    = options.name;
    that.context = options.context;

    // Keeps track of the turtle's current position and velocity.
    that.orientation = 0;
    that.angularVelocity = 0;
    that.linearVelocity  = 0;
		that.x = null; //that.context.canvas.width / 2;
		that.y = null; //that.context.canvas.height / 2;
		that.trailX = new Array();
		that.trailY = new Array();
		
    var turtle_names = ['diamondback.png', 'fuerte.png', 'robot-turtle.png', 'turtle.png', 'box-turtle.png', 'electric.png', 'groovy.png', 'sea-turtle.png'];
    var randomIndex = Math.floor(Math.random() * turtle_names.length);
    var randomTurtle = turtle_names[randomIndex];

    // Represents the turtle as a PNG image.
    that.image = new Image();
    that.image.src = 'images/'+randomTurtle;
    that.draw();
		
		that.listener = new ROSLIB.Topic({
			ros : that.ros,
			name : '/' + that.name + '/pose',
			messageType : 'turtlesim/Pose'
		});
		
		that.listener.subscribe(function(message) {
			that.x = message.x * that.context.canvas.width / 11.08;
			that.y = that.context.canvas.height - message.y * that.context.canvas.height / 11.08;
			that.orientation = message.theta;
			if (that.trailX.length==0) {
				that.trailX.push(that.x);
				that.trailY.push(that.y);
			} else {
				var lastPos = that.trailX.length - 1;
				if (that.x!=that.trailX[lastPos] || that.y!=that.trailY[lastPos]) {
					that.trailX.push(that.x);
					that.trailY.push(that.y);					
				}
			}
			that.draw();
		});
  };
	
  Turtle.prototype.draw = function() {
    this.context.fillStyle = "BLUE"
		this.context.fillRect(0, 0, this.context.canvas.width, this.context.canvas.height);
    this.context.fillStyle = "WHITE"
		for (i=0;i<this.trailX.length;i++) {
			this.context.fillRect(this.trailX[i]-1, this.trailY[i]-1, 3, 3);			
		}
    this.context.save();
    var x = this.x;
    var y = this.y;
		
		if ((x!=null)&&(x!=null)) {
    var imageWidth  = this.image.width;
    var imageHeight = this.image.height;

    this.context.translate(x, y);
    this.context.rotate(-this.orientation);
    this.context.drawImage(
      this.image,
     -(imageWidth / 2),
     -(imageHeight / 2),
     imageWidth,
     imageHeight
    );
	}
    this.context.restore();
  };
	
  return Turtle;
}());

