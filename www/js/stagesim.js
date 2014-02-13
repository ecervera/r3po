var StageSim = (function() {

	var StageSim = function(options) {
		var that = this;
		options = options || {};
		that.ros     = options.ros;
		that.context = options.context;
		that.background = new Image();
		that.background.src = options.background;
		that.mpix = options.mpix;
		that.bot  = new Array();
		//that.draw();
	};

	StageSim.prototype.spawnBot = function(name,image) {
		var that = this;
		that.bot.push(new StageBot({
			name    : name,
			ros     : that.ros,
			context : that.context,
			sim     : that,
			index   : that.bot.length,
			background : that.background,
			image : image,
			mpix : that.mpix
		}));
	};

 	StageSim.prototype.draw = function() {

		this.context.clearRect(0,0,this.context.canvas.width,this.context.canvas.height);
		var bw = this.background.width;
		var bh = this.background.height;
		var cw = this.context.canvas.width; // square canvas, width=height
		var ratio = bh/bw;
		this.context.drawImage(this.background,0,cw*(1-ratio)/2,cw,cw*ratio);

		if($("#dispGrid").is(':checked')){
			var scale = cw/bw;
			var mpix = this.mpix/scale;
			var n = 6; // grid lines from -n to n
			for (var x=-n;x<=n;x++) {
				this.context.beginPath();
				this.context.moveTo(x/mpix+cw/2,-n/mpix+cw/2);
				this.context.lineTo(x/mpix+cw/2, n/mpix+cw/2);
				this.context.strokeStyle = 'rgba(192,192,192,0.5)';
				this.context.stroke();
			}
			for (var y=-n;y<=n;y++) {
				this.context.beginPath();
				this.context.moveTo(-n/mpix+cw/2, y/mpix+cw/2);
				this.context.lineTo( n/mpix+cw/2, y/mpix+cw/2);
				this.context.strokeStyle = 'rgba(192,192,192,0.5)';
				this.context.stroke();
			}
		}
 		//this.bot.draw();
		for (var i=0;i<this.bot.length;i++) {
			this.bot[i].draw();
		}
 	};
	return StageSim;
}());

