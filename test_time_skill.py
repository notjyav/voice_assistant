from skills.time_skill import TimeSkill

skill = TimeSkill()

print(skill.can_handle("what time is it"))
print(skill.can_handle("tell me a joke"))

skill.handle("what time is it")