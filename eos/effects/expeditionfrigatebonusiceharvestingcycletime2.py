type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"), "duration", src.getModifiedItemAttr("eliteBonusExpedition2"), skill="Expedition Frigates")
