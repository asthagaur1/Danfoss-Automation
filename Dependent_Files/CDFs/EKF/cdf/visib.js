var custom_vr = { "CheckVisibilityRules" : function(RuleId)  {
var GetVar = function(x){ return this.p(x); }.bind(this);

	if (RuleId == 0) return 1;
	if (RuleId == 1) return GetVar(2) == 1;
	if (RuleId == 2) return GetVar(97) == 1;
	if (RuleId == 3) return GetVar(97) == 1 && GetVar(9) == 1;
	if (RuleId == 4) return 0;
	return 1;

}}