from Tools.printer import printer
from Tools.colors import colors as c
from Tools.cleaner import clear
import os
import sys
import time
import shutil

width = os.get_terminal_size().columns

def main():
	printer("=")
	print()
	print(c.y+f"브롤스타즈 v11 브롤러 메이커!".center(width))
	print(c.y+f"원본 제작자 ORIGINAL MADE BY s.b[discord] |||| 한국어 번역 KOREAN TRANSLATION BY bsfristine_[discord]".center(width))
	print()
	printer("=")
	print()
	print(f"{c.r} [NOTICE] 이 프로그램에서 사용하는 브롤 버전은 v29입니다! {c.r}".center(width))
	print(f"""{c.c}0 : csvs 초기화
1 : 시작
2 : 나가기{c.w}""")
	print()
	printer("=")
	print()
	start_question = input(f"{c.b}선택: {c.w}")
	if start_question != "0" and start_question != "1" and start_question != "2":
		print(f"{c.r}잘못된 값{c.w}")
		time.sleep(0.5)
		clear()
		main()
	elif start_question == "0":
		dir = os.getcwd()
		print(f"{c.c}[TOOL] 예전 csv파일을 삭제하는 중...{c.w}")
		shutil.rmtree("csvs")
		time.sleep(0.5)
		print(f"{c.c}[TOOL] csvs 폴더를 리마스킹 하는 중...{c.w}")
		os.mkdir("csvs")
		time.sleep(0.5)
		print(f"{c.c}[TOOL] 새로운 csv파일을 옮기는 중...")
		for file in os.listdir("replacor"):
			time.sleep(0.5)
			shutil.copyfile(f"{dir}/replacor/{file}", f"{dir}/csvs/{file}")
			print(f"{c.g}[TOOL] 성공적으로 완료하였습니다. {file.upper()}{c.w}")
		time.sleep(0.5)
		print(f"{c.c}[TOOL] 완료!{c.w}")
		time.sleep(0.5)
		print(f"{c.r}[TOOL] 콘솔 초기화중...{c.w}")
		time.sleep(2)
		clear()
		main()
	elif start_question == "1":
		print(f"{c.y}[TOOL] 먼저, 기본 에딧을 시작합니다{c.w}")
		time.sleep(1)
		brawler_rarity = input(f"{c.c}브롤러 희귀도 (epic, rare, super_rare, legendary): {c.w}")
		brawlername = str(input(f"{c.c}브롤러 이름: {c.w}"))
		brawler_name = brawlername.upper()
		brawler_desc = input(f"{c.c}브롤러 설명: {c.w}")
		brawleratkname = input(f"{c.c}브롤러 공격 이름: {c.w}")
		brawler_atk_name = brawleratkname.upper()
		brawler_atk_desc = input(f"{c.c}브롤러 공격 설명: {c.w}")
		brawlerultiname = input(f"{c.c}브롤러 특수공격 이름: {c.w}")
		brawler_ulti_name = brawlerultiname.upper()
		brawler_ulti_desc = input(f"{c.c}브롤러 특수공격 설명: {c.w}")
		brawler_health = input(f"{c.c}브롤러 체력 수치: {c.w}")
		brawler_speed = input(f"{c.c}브롤러 이동속도 수치: {c.w}")
		print(f"{c.y}[TOOL] 기본 에딧이 끝났습니다!\n공격 스킬 에딧을 시작하는 중...{c.w}")
		time.sleep(1)
		atk_damage = input(f"{c.c}공격 데미지: {c.w}")
		canmoveatk = input(f"{c.c}공격 도중 움직임 여부 (true or fase): {c.w}")
		if canmoveatk.lower() == "true":
			can_move_atk = "true"
		elif canmoveatk.lower() != "true":
			can_move_atk = ""
		canatkshoot = input(f"{c.c}오토샷 가능 여부 (true or false): {c.w}")
		if canatkshoot == "true":
			can_atk_shoot = "true"
		else:
			can_atk_shoot = ""
		atk_range = input(f"{c.c}공격 사정거리: {c.w}")
		atk_rec = input(f"{c.c}재장전 시간 (in ms): {c.w}")
		atk_bullets = input(f"{c.c}공격 당 탄 개수: {c.w}")
		max_charge = input(f"{c.c}최대 에모 갯수: {c.w}")
		atk_spread = input(f"{c.c}공격이 퍼지는 거리: {c.w}")
		print(f"{c.y}[TOOL] 공격 에딧을 마쳤습니다!\n피사체 에딧을 시작하는 중...{c.w}")
		time.sleep(1)
		atk_proj_speed = input(f"{c.c}피사체 속도: {c.w}")
		atk_proj_scale = input(f"{c.c}피사체 크기: {c.w}")
		atkbounce = input(f"{c.c}공격이 바운스 되는 정도 (true or false): {c.w}")
		if atkbounce == "true":
			atk_bounce = "true"
			atk_bounce_dist = input(f"{c.c}바운싱 후에 추가 공격 거리: {c.w}")
		else:
			atk_bounce = ""
			atk_bounce_dist = ""
		atkpass = input(f"{c.c}피사체가 적을 뚫고 지나가는 여부 (true or false): {c.w}")
		if atkpass == "true":
			atk_pass = "true"
		else:
			atk_pass = ""
		atkdestroy = input(f"{c.c}벽 파괴 가능 여부 (true or false): {c.w}")
		if atkdestroy == "true":
			atk_destroy = "true"
		else:
			atk_destroy = ""
		atk_push = input(f"{c.c}특수공격으로 인해 밀쳐지는 힘의 정도 (Enter로 스킵): {c.w}")
		atk_freeze = input(f"{c.c}특수공격으로 인해 얼리게 되는 힘의 정도 (Enter로 스킵): {c.w}")
		atk_stun = input(f"{c.c}공격이 적을 스턴걸리게 하는 힘의 정도 (Enter로 스킵): {c.w}")
		atk_life = input(f"{c.c}공격 당 체력을 흡수하는 정도 (% 당, Enter로 스킵): {c.w}")
		atkpassenv = input(f"{c.c}공격이 벽을 뚫는 여부 (true or false): {c.w}")
		if atkpassenv == "true":
			atk_pass_env = "true"
		else:
			atk_pass_env = ""
		atk_poison = input(f"{c.c}공격 당 독 데미지 IN % (Enter로 스킵): {c.w}")
		atkgrow = input(f"{c.c}ATTACK CAN GROW STRONGER[해석 못하겠음 ㅈㅅ] (파이퍼 처럼, true or false): {c.w}")
		if atkgrow == "true":
			atk_grow = "true"
		else:
			atk_grow = ""
		print(f"{c.y}[TOOL] 피사체 에딧을 마쳤습니다!\n특수공격 에딧을 시작하는 중...{c.w}")
		time.sleep(1)
		ulti_damage = input(f"{c.c}특수 공격 데미지: {c.w}")
		canmoveulti = input(f"{c.c}특수공격 도중 움직임 가능 여부(true or fase): {c.w}")
		if canmoveulti.lower() == "true":
			can_move_ulti = "true"
		elif canmoveulti.lower() != "true":
			can_move_ulti = ""
		canultishoot = input(f"{c.c}특수공격 오토샷 가능 여부 (true or false): {c.w}")
		if canultishoot == "true":
			can_ulti_shoot = "true"
		else:
			can_ulti_shoot = ""
		ulti_range = input(f"{c.c}특수공격 거리: {c.w}")
		ulti_bullets = input(f"{c.c}특수공격 당 탄의 갯수: {c.w}")
		ulti_spread = input(f"{c.c}특수 공격이 퍼지는 거리: {c.w}")
		print(f"{c.y}[TOOL] 특수공격 에딧을 마쳤습니다!\n특수공격 피사체 에딧을 시작하는 중...{c.w}")
		ulti_proj_speed = input(f"{c.c}특수공격 피사체 속도: {c.w}")
		ulti_proj_scale = input(f"{c.c}특수공격 피사체 크기: {c.w}")
		ultibounce = input(f"{c.c}특수 공격 바운싱 여부 (true or false): {c.w}")
		if ultibounce == "true":
			ulti_bounce = "true"
			ulti_bounce_dist = input(f"{c.c}바운싱 후 추가 특수공격 거리: {c.w}")
		else:
			ulti_bounce = ""
			ulti_bounce_dist = ""
		ultipass = input(f"{c.c}특수공격이 적을 뚫는 여부 (true or false): {c.w}")
		if ultipass == "true":
			ulti_pass = "true"
		else:
			ulti_pass = ""
		ultidestroy = input(f"{c.c}특수공격 벽 파괴 가능 여부 (true or false): {c.w}")
		if ultidestroy == "true":
			ulti_destroy = "true"
		else:
			ulti_destroy = ""
		ulti_push = input(f"{c.c}특수공격으로 인해 밀쳐지는 거리 (Enter로 스킵): {c.w}")
		ulti_freeze = input(f"{c.c}특수공격으로 인해 얼리게 되는 힘의 정도 (Enter로 스킵): {c.w}")
		ulti_stun = input(f"{c.c}특수공격이 적을 스턴걸리게 하는 힘의 정도 (Enter로 스킵): {c.w}")
		ulti_life = input(f"{c.c}공격 당 체력을 흡수하는 정도 (% 당, Enter로 스킵): {c.w}")
		ultipassenv = input(f"{c.c}특수공격이 벽을 뚫을 수 있는 여부 (true or false): {c.w}")
		if ultipassenv == "true":
			ulti_pass_env = "true"
		else:
			ulti_pass_env = ""
		ulti_poison = input(f"{c.c}특수공격 당 독 데미지 IN % (Enter로 스킵): {c.w}")
		ultigrow = input(f"{c.c}ULTI CAN GROW STRONGER[해석 못하겠음 ㅈㅅ] (파이퍼 특수공격처럼, true or false): {c.w}")
		if ultigrow == "true":
			ulti_grow = "true"
		else:
			ulti_grow = ""
		print(f"{c.y}[TOOL] 특수공격 에딧을 마쳤습니다!\n 스타파워 에딧을 시작하는 중...{c.w}")
		time.sleep(1)
		brawler_star_power = input(f"{c.c}ULTI CAN GROW STRONGER[해석 못하겠음 ㅈㅅ] (파이퍼 특수공격처럼, true or false): {c.w}")
		print(f"{c.y}[TOOL] texts.csv수정하는 중...{c.w}")
		time.sleep(1)
		texts_file = open("csvs/texts.csv", "a")
		brawler_ulti_name_rep = brawler_ulti_name.replace(' ', '_')
		brawler_atk_name_rep = brawler_atk_name.replace(' ', '_')
		brawler_name_rep = brawler_name.replace(' ', '_')
		texts_file.write(f'\n"TID_{brawler_name_rep}","{brawler_name}"')
		texts_file.write(f'\n"TID_{brawler_name_rep}_SHORT_DESC","MADE WITH BRAWL STARS V11 BRAWLER MAKER TOOL"')
		texts_file.write(f'\n"TID_{brawler_name_rep}_DESC","{brawler_desc}"')
		texts_file.write(f'\n"TID_{brawler_atk_name_rep}","{brawler_atk_name}"')
		texts_file.write(f'\n"TID_{brawler_atk_name_rep}_DESC","{brawler_atk_desc}"')
		texts_file.write(f'\n"TID_{brawler_ulti_name_rep}","{brawler_ulti_name}"')
		texts_file.write(f'\n"TID_{brawler_ulti_name_rep}_DESC","{brawler_ulti_desc}"')
		texts_file.flush()
		texts_file.close()
		print(f"{c.y}[TOOL]  characters.csv을 수정하는 중...{c.w}")
		time.sleep(1)
		char_file = open("csvs/characters.csv", "a")
		char_file.write(f'\n"{brawlername.replace(" ", "_")}",,,"{brawlername.replace(" ", "_")}Weapon","{brawlername.replace(" ", "_")}Ulti",,{brawler_speed},{brawler_health},,,,,,,,12,,128,120,"Hero",,"{brawler_name_rep}_Default",,,,,,,"takedamage_gen","death_shotgun_girl","Gen_move_fx","reload_shotgun_girl","No_ammo_shotgungirl","Dry_fire_shotgungirl",,,,,,,,,,,"Shelly_Kill","Shelly_Lead","Shelly_Start","Utilshotgun_Vo","ShellyTakedamge_Vo","Shelly_Die",,30,,80,80,,,35,116,210,80,175,,,120,"Medium",-48,,350,,,"TID_{brawler_name_rep}",,"sc/ui.sc","hero_icon_shelly",1000,"human","footstep",25,250,200,,,,1,3,2')
		char_file.flush()
		char_file.close()
		print(f"{c.y}[TOOL] skins.csv를 수정하는 중...{c.w}")
		time.sleep(1)
		skin_name = f"{brawler_name_rep}_Default"
		brawler_skin = f"{brawlername.replace(' ', '_')}"
		skin_file = open("csvs/skins.csv", "a")
		skin_file.write(f'\n"{skin_name}","{brawler_skin}",,,,,"shelly_geo.scw:body+gun+head","shelly_tex.pvr","shelly_tex.pvr","shelly_tex.pvr","shelly_tex.pvr","ShellyIdle","ShellyWalk","ShellyPrimary","ShellySecondary","ShellyRecoil",,"ShellyRecoil",,"ShellyReload","ShellyPushback","ShellyWin","ShellyWinloop","ShellyLose","ShellyLoseloop","ShellyIdle","ShellyWin","ShellyWinloop","ShellyWin","ShellyIdle",,,,"ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace","ShellyFace",0,100,,,')
		skin_file.flush()
		skin_file.close()
		print(f"{c.y}[TOOL] cards.csv를 수정하는 중...{c.w}")
		time.sleep(1)
		cards_file = open("csvs/cards.csv", "a")
		brawler_card = f"{brawler_star_power.replace(' ', '_')}"
		cards_file.write(f'\n"{brawler_card}_unlock","sc/ui.sc",,"{brawler_card}",0,,"unlock",,,,"{brawler_rarity}",,,,,,21')
		cards_file.write(f'\n"{brawler_card}_hp","sc/ui.sc","health_icon","{brawler_card}",1,,"hp",,,,"common","TID_ARMOR","TID_ARMOR_STAT",,"genicon_health",,')
		cards_file.write(f'\n"{brawler_card}_abi","sc/ui.sc","attack_icon","{brawler_card}",2,,"skill","{brawler_star_power.replace(" ", "_")}Weapon",,,"common","TID_{brawler_atk_name_rep}","TID_STAT_DAMAGE_PER_SHOT",,"genicon_damage",,')
		cards_file.write(f'\n"{brawler_card}_ulti","sc/ui.sc","ulti_icon","{brawler_card}",3,,"skill","{brawler_star_power.replace(" ", "_")}Ulti",,,"common","TID_{brawler_ulti_name_rep}","TID_STAT_DAMAGE_PER_SHOT",,"genicon_damage",,')
		cards_file.write(f"\n{brawler_card}_unique,sc/ui.sc,icon_eiuD,{brawler_card},4,,freeze,,50,350,common,TID_SPEC_ABI_FREEZE,,,genicon_health")
		cards_file.flush()
		cards_file.close()
		print(f"{c.y}[TOOL] skills.csv를 수정하는 중 (1/2)...{c.w}")
		skill_file = open("csvs/skills.csv", "a")
		skill_file.write(f"\n{brawlername.replace(' ', '_')}Weapon,Attack,{can_move_atk},true,{can_atk_shoot},250,150,,{atk_range},,{atk_rec},{max_charge},{atk_damage},100,{atk_spread},,{atk_bullets},,true,,,,,,,{brawler_skin}Projectile,,,,,,,,,sc/ui.sc,rapid_fire_button,shotgun_girl_attack,,,,")
		print(f"{c.y}[TOOL] skills.csv를 수정하는 중 (2/2)...{c.w}")
		time.sleep(1)
		skill_file.write(f"\n{brawlername.replace(' ', '_')}Ulti,Attack,{can_move_ulti},true,{can_ulti_shoot},250,150,,{ulti_range},,,,{ulti_damage},100,{ulti_spread},,{ulti_bullets},,true,,,,,,,{brawler_skin}UltiProjectile,,,,,,skillicon_megablast,,,sc/ui.sc,rapid_fire_button,shotgun_girl_attack_ulti,,,,")
		skill_file.flush()
		skill_file.close()
		print(f"{c.y}[TOOL] projectiles.csv를 수정하는 중 (1/2)...{c.w}")
		proj_file = open("csvs/projectiles.csv", "a")
		proj_file.write(f"\n{brawler_skin}Projectile,{atk_proj_speed},sc/effects.sc,Bouncy_bullet_blue,Bouncy_bullet_red,projectile_shadow,,,,,,Gen_hit,Gen_hit,no_hit,0,,,,,0,2,0,{atk_proj_scale},,,,,,shotgun_trail_small,true,,{atk_bounce},{atk_bounce_dist},,{atk_pass},{atk_destroy},,{atk_push},,,,,,,,,{atk_freeze},{atk_stun},,,,{atk_life},{atk_pass_env},{atk_poison},,,{atk_grow},")
		print(f"{c.y}[TOOL] projectiles.csv를 수정하는 중 (2/2)...{c.w}")
		proj_file.write(f"\n{brawler_skin}UltiProjectile,{ulti_proj_speed},sc/effects.sc,Bouncy_bullet_blue,Bouncy_bullet_red,projectile_shadow,,,,,,Gen_hit,Gen_hit,no_hit,0,,,,,0,2,0,{ulti_proj_scale},,,,,,shotgun_trail_small,true,,{ulti_bounce},{ulti_bounce_dist},,{ulti_pass},{ulti_destroy},,{ulti_push},,,,,,,,,{ulti_freeze},{ulti_stun},,,,{ulti_life},{ulti_pass_env},{ulti_poison},,,{ulti_grow},")
	elif start_question == "2":
		exit()
     
if __name__ == '__main__':
	main()
