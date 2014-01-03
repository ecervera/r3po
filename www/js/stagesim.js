var StageSim = (function() {

	var StageSim = function(options) {
		var that = this;
		options = options || {};
		that.ros     = options.ros;
		that.context = options.context;
		that.background = new Image();
		that.background.src = options.background
		that.bot  = null;
		//that.draw();
	};

	StageSim.prototype.spawnBot = function(name) {
		var that = this;
		that.bot = new StageBot({
			name    : name,
			ros     : that.ros,
			context : that.context,
			background : that.background
		});
	};

// 	StageSim.prototype.draw = function() {
// 		this.context.drawImage(this.background,0,0);
// 		//this.bot.draw();
// 	};
	return StageSim;
}());

