type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Warfare Specialist"),
                                  "commandBonusHidden", module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)
