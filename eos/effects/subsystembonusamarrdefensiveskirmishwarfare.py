type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Skirmish Warfare Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("subsystemBonusAmarrDefensive") * level)
