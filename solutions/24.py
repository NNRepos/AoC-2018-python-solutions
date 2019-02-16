import sys
import re
import operator as op
input="""\
Immune System:
504 units each with 1697 hit points (weak to fire; immune to slashing) with an attack that does 28 fire damage at initiative 4
7779 units each with 6919 hit points (weak to bludgeoning) with an attack that does 7 cold damage at initiative 2
7193 units each with 13214 hit points (weak to cold, fire) with an attack that does 12 slashing damage at initiative 14
1898 units each with 3721 hit points (weak to bludgeoning) with an attack that does 16 cold damage at initiative 20
843 units each with 3657 hit points (immune to slashing) with an attack that does 41 cold damage at initiative 17
8433 units each with 3737 hit points (immune to radiation; weak to bludgeoning) with an attack that does 3 bludgeoning damage at initiative 8
416 units each with 3760 hit points (immune to fire, radiation) with an attack that does 64 radiation damage at initiative 3
5654 units each with 1858 hit points (weak to fire) with an attack that does 2 cold damage at initiative 6
2050 units each with 8329 hit points (immune to radiation, cold) with an attack that does 36 radiation damage at initiative 12
4130 units each with 3560 hit points with an attack that does 8 bludgeoning damage at initiative 13

Infection:
442 units each with 35928 hit points with an attack that does 149 bludgeoning damage at initiative 11
61 units each with 42443 hit points (immune to radiation) with an attack that does 1289 slashing damage at initiative 7
833 units each with 6874 hit points (weak to slashing) with an attack that does 14 bludgeoning damage at initiative 15
1832 units each with 61645 hit points with an attack that does 49 fire damage at initiative 9
487 units each with 26212 hit points (weak to fire) with an attack that does 107 bludgeoning damage at initiative 16
2537 units each with 18290 hit points (immune to cold, slashing, fire) with an attack that does 11 fire damage at initiative 19
141 units each with 14369 hit points (immune to bludgeoning) with an attack that does 178 radiation damage at initiative 5
3570 units each with 34371 hit points with an attack that does 18 radiation damage at initiative 10
5513 units each with 60180 hit points (weak to radiation, fire) with an attack that does 16 slashing damage at initiative 1
2378 units each with 20731 hit points (weak to bludgeoning) with an attack that does 17 radiation damage at initiative 18""" 
try:
  #vars
  input=input.split('\n\n')
  immune=input[0].split('\n')[1:]
  infection=input[1].split('\n')[1:]
  immune_groups=[]
  infection_groups=[]
  pattern=re.compile("(?P<units>\d+) units each with (?P<hp>\d+) hit points (?:\((?P<parens>(?:(?:\w+)(?: |;|,)*)+)\))? ?with an attack that does (?P<dmg>\d+) (?P<type>[a-z]+) damage at initiative (?P<init>\d+)")
  #parse good guys
  for group in immune:
    match=pattern.match(group)
    units=int(match.group('units'))
    hp=int(match.group('hp'))
    parens=match.group('parens')
    weaknesses=immunities=None
    if parens:
      parens=parens.split('; ')
      for p in parens:
        p=p.split(' ')
        if p[0]=='weak':
          weaknesses=[weakness.strip(',') for weakness in p[2:]]
        elif p[0]=='immune':
          immunities=[immunity.strip(',') for immunity in p[2:]]
        else:
          raise Exception("bad weakness/immunity string")
    dmg=int(match.group('dmg'))
    dmg_type=match.group('type')
    init=int(match.group('init'))
    immune_group=[units,hp,weaknesses,immunities,dmg,dmg_type,init,False]
    immune_groups.append(immune_group)
  #parse bad guys
  for group in infection:
    match=pattern.match(group)
    units=int(match.group('units'))
    hp=int(match.group('hp'))
    parens=match.group('parens')
    weaknesses=immunities=None
    if parens:
      parens=parens.split('; ')
      for p in parens:
        p=p.split(' ')
        if p[0]=='weak':
          weaknesses=[weakness.strip(',') for weakness in p[2:]]
        elif p[0]=='immune':
          immunities=[immunity.strip(',') for immunity in p[2:]]
        else:
          raise Exception("bad weakness/immunity string")
    dmg=int(match.group('dmg'))
    dmg_type=match.group('type')
    init=int(match.group('init'))
    infection_group=[units,hp,weaknesses,immunities,dmg,dmg_type,init,False]
    infection_groups.append(infection_group)
  #each group looks like this: [units,hp,weaknesses,immunities,dmg,dmg_type,init,death_status]
  #tick
  rounds=0
  while (8):
    targets=[]
    #each target looks like this: [attacking group,attacker, defender, dmg*double, init]
    #choose targets - immune
    chosen_targets=[]
    immune_groups=list(reversed(sorted(immune_groups, key=lambda x:[x[0]*x[4], x[6]])))
    infection_groups=list(reversed(sorted(infection_groups, key=lambda x:[x[0]*x[4], x[6]])))
    for g,group in enumerate(immune_groups):
      units,hp,weaknesses,immunities,dmg,dmg_type,init,is_dead=group
      if is_dead:
        continue
      dmg_dealt=0
      target=None
      for e,enemy in enumerate(infection_groups):
        if enemy[7]: #enemy dead
          continue
        if e in chosen_targets: #already chosen
          continue
        if not target==None:
          prev_target=infection_groups[target]
        if enemy[3]: #has immunities
          if dmg_type in enemy[3]: #immunities
            continue
        this_dmg = dmg*units #dmg=effective power
        if enemy[2]: #has weaknesses
          if dmg_type in enemy[2]: #weaknesses
            this_dmg*=2
        if this_dmg>dmg_dealt: #change target
          dmg_dealt=this_dmg
          target=e
        elif this_dmg==dmg_dealt: #check effective power
          this_eff=enemy[0]*enemy[4]
          prev_eff=prev_target[0]*prev_target[4] #no error here because prev_target exists
          if this_eff>prev_eff: #change target
            dmg_dealt=this_dmg
            target=e
          elif this_eff==prev_eff: #check init
            this_init=enemy[6]
            prev_init=prev_target[6]
            if this_init>prev_init: #change target
              dmg_dealt=this_dmg
              target=e
      if not target==None:
        targets.append(['immune', g, target, dmg_dealt/units, group[6]])
        chosen_targets.append(target)
    #choose targets - infection
    chosen_targets=[]
    for g,group in enumerate(infection_groups):
      units,hp,weaknesses,immunities,dmg,dmg_type,init,is_dead=group
      if is_dead:
        continue
      dmg_dealt=0
      target=None
      for e,enemy in enumerate(immune_groups):
        if enemy[7]: #enemy dead
          continue
        if e in chosen_targets: #already chosen
          continue
        if not target==None:
          prev_target=immune_groups[target]
        if enemy[3]: #has immunities
          if dmg_type in enemy[3]: #immunities
            continue
        this_dmg = dmg*units #dmg=effective power
        if enemy[2]: #has weaknesses
          if dmg_type in enemy[2]: #weaknesses
            this_dmg*=2
        if this_dmg>dmg_dealt: #change target
          dmg_dealt=this_dmg
          target=e
        elif this_dmg==dmg_dealt: #check effective power
          this_eff=enemy[0]*enemy[4]
          prev_eff=prev_target[0]*prev_target[4] #no error here because prev_target exists
          if this_eff>prev_eff: #change target
            dmg_dealt=this_dmg
            target=e
          elif this_eff==prev_eff: #check init
            this_init=enemy[6]
            prev_init=prev_target[6]
            if this_init>prev_init: #change target
              dmg_dealt=this_dmg
              target=e
      if not target==None:
        targets.append(['infection', g, target, dmg_dealt/units, group[6]])
        chosen_targets.append(target)
    #attack
    targets=list(reversed(sorted(targets, key=op.itemgetter(4)))) #sort by decreasing init
    for target in targets:
      atk_group, attacker, defender, dmg_dealt, init=target
      if atk_group=='immune': #attack infection
        if immune_groups[attacker][7]: #attacker died this round
          continue
        real_dmg=dmg_dealt*immune_groups[attacker][0]
        defender_hp=infection_groups[defender][1]
        units_lost= real_dmg/defender_hp
        infection_groups[defender][0]-=units_lost
        if infection_groups[defender][0]<=0:
          infection_groups[defender][7]=True
      else: #attack immune
        if infection_groups[attacker][7]: #attacker died this round
          continue
        real_dmg=dmg_dealt*infection_groups[attacker][0]
        defender_hp=immune_groups[defender][1]
        units_lost=real_dmg/defender_hp
        immune_groups[defender][0]-=units_lost
        if immune_groups[defender][0]<=0:
          immune_groups[defender][7]=True
    over=True
    ans=0
    for group in immune_groups:
      if not group[7]: #someone is alive
        over=False
    if over: #all immune groups are dead
      for group in infection_groups: #count living units
        if not group[7]:
          ans+=group[0]
      print "The infection has won after", rounds, "rounds, with", ans, "units remaining."
      raw_input()
      raise Exception("war is over")
    else: #some immune groups alive
      over=True
      for group in infection_groups:
        if not group[7]: #someone is alive
          over=False
      if over: #all infection groups are dead
        for group in immune_groups: #count living units
          if not group[7]:
            ans+=group[0]
        print "The immune system has won after", rounds, "rounds, with", ans, "units remaining."
        raw_input()
        raise Exception("war is over")
    #war not over
    rounds+=1
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()