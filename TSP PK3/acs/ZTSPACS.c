#library "ZTSPACS"

#include "zcommon.acs"
#include "mathFuncs.h"
#include "miscFuncs.h"

global int 50:GArray50[];
/*
  1-64 = Player TIDs
*/
    
int LastxFixedA[64];
int LastyFixedA[64];
int LastzFixedA[64];
int LastCurveA[64];

function int abs(int x)
{
    if (x < 0) { return -x; }
    return x;
}

//Shotgun Functions

function void ShellMessage(int which, int howmany)
{
  switch(which){
    case 1:
      if(howmany > 1){ hudmessage(s:"Picked up ",d:howmany,s:" \cnshock\c- shells.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a \cnshock\c- shell.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break;
    case 2:
      if(howmany > 1){ hudmessage(s:"Picked up ",d:howmany,s:" \cihellfire\c- shells.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a \cihellfire\c- shell.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break;
    case 3:
      if(howmany > 1){ hudmessage(s:"Picked up ",d:howmany,s:" \cppoison\c- shells.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a \cppoison\c- shell.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break;
    case 4:
      if(howmany > 1){ hudmessage(s:"Picked up ",d:howmany,s:" \cgbuckshot\c- shells.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a \cgbuckshot\c- shell.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break; }
}

//Dahlia Functions

function void BoltMessage(int which, int howmany)
{
  switch(which){
    case 1:
      if(howmany > 1){ hudmessage(s:"Picked up a box of crossbow bolts. [\cv+",d:howmany,s:" Crossbow Bolts\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a crossbow bolt. [\cv+1 Crossbow Bolt\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break;
    case 2:
      if(howmany > 1){ hudmessage(s:"Picked up a box of explosive bolts. [\cj+",d:howmany,s:" Explosive Bolts\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up an explosive bolt. [\cj+1 Explosive Bolt\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break;
    case 3:
      if(howmany > 1){ hudmessage(s:"Picked up a box of crossbow bolts. [\cv+",d:howmany,s:" Crossbow Bolts\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      else{ hudmessage(s:"Picked up a crossbow bolt. [\cv+1 Crossbow Bolt\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
      break; }
}

//ToolBox Functions

function void RocketMessage(int howmany)
{
  if(howmany > 1){ hudmessage(s:"Picked up a crate of Rockets. [\cg+",d:howmany,s:" Launcher Ammo\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
  else{ hudmessage(s:"Picked up a  Rocket. [\cg+1 Launcher Ammo\c-]";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_RED,0.0,0.0,1.0); }
}


script "MonsterEnter" (void)
{
  if(GameSkill() >= 0){ GiveInventory("Diff0",1); }
  if(GameSkill() >= 1){ GiveInventory("Diff1",1); }
  if(GameSkill() >= 2){ GiveInventory("Diff2",1); }
  if(GameSkill() >= 3){ GiveInventory("Diff3",1); }
  if(GameSkill() >= 4){ GiveInventory("Diff4",1); }
  if(GameSkill() >= 5){ GiveInventory("Diff5",1); }
  if(CheckActorProperty(0, APROP_SPECIES,"ZombieHitscan") && GetCVar("tsp_zmelee")){ GiveInventory("GiveAvoidMelee",1); }
  
  
}

script "CheckClass" (int which)
{
  int result;
  switch (which){
    case 1:
      if(CheckActorClass(0,"SpacePirate")){ result = 1; }
      break;
    case 2:
      if(CheckActorClass(0,"RoboMel")){ result = 1; }
      break; }
  SetResultValue(result);
}


script "GetToasterCVAR" (void)
{
  SetResultValue(GetCVar("tsp_toaster"));
}

script "GetZMeleeCVAR" (void)
{
  SetResultValue(GetCVar("tsp_zmelee"));
}

script "GetBeamInfiniteCVAR" (void)
{
  SetResultValue(GetCVar("tsp_beaminf"));
}

script "GetGoldenPistolCVAR" (void)
{
  SetResultValue(GetCVar("tsp_goldenpistol"));
}

script "GetFistsStartCVAR" (void)
{
  SetResultValue(GetCVar("tsp_fistsstart"));
}

script "GetMagPushCVAR" (void)
{
  SetResultValue(GetCVar("tsp_melmagpush"));
}

script "GetActionModeCVAR" (void)
{
  SetResultValue(GetCVar("tsp_actionmode"));
}

script "GetSuperSecretCVAR" (void)
{
  SetResultValue(GetCVar("tsp_supersecret"));  
}

script "GetMeleeSoundsCVAR" (void)
{
  SetResultValue(GetCVar("tsp_meleesounds"));
}

script "GetMeleeSupremeCVAR" (void)
{
  SetResultValue(GetCVar("tsp_meleesupreme"));
}

script "TSPGetGameSkill" (void)
{
  SetResultValue(GameSkill());
}

/*script "TSPEnterScript1" ENTER
{

  hudmessage (s:"Blue Vertigo Presents: The Space Pirate\n \nCvars:\n \ntsp_shellpool - If set to true/1 (default), all shell types share the same ammo pool. If set to false/0, they do not and each has a separate ammo pool.
  \n\r_drawvoxels - If set to true/1 (default), voxels will be used for crossbow bolts and items. If set to true/1, models will be used for the crossbow bolts and sprites will be used for items. If you're playing this in GZDoom models will render faster, so switch if you're having performance issues, but if you're playing in ZDoom the voxels will render just fine.";HUDMSG_PLAIN|HUDMSG_LOG,2,CR_GREEN,1.5,0.375,0.1);

  TakeInventory("PlayingPickupSound", 1);
  Terminate;
}

script "TSPArmorScript" (void)
{
  if(CheckInventory("BasicArmor") >= 1)
  {
    Delay(6);
    Restart;
  }
  else
  {
    TakeInventory("TSPGreenDamageReduction",1);
    TakeInventory("TSPGreenArmorDamage",1);
    TakeInventory("TSPBlueDamageReduction",1);
    TakeInventory("TSPBlueArmorDamage",1);
    Terminate;
  }
} */

script "TSPPickupSounds" (int which)
{
  if(CheckInventory("PlayingPickupSound") > 0){ terminate; }
  else{
    GiveInventory("PlayingPickupSound", 1);
	
    if(CheckActorClass(0,"SpacePirate") && GetPlayerInfo(PlayerNumber(),PLAYERINFO_GENDER) == 2){ //Mel (with Robo Voice)
      switch (which){
        case 1:
          LocalAmbientSound("melflavpickuprobo/Pistol",127);
          Delay(41);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 2:
          LocalAmbientSound("melflavpickuprobo/ZekeShotgun",127);
          Delay(49);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 3:
          LocalAmbientSound("melflavpickuprobo/Crossbow",127);
          Delay(35);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 4:
          LocalAmbientSound("melflavpickuprobo/Ammobox50",127);
          Delay(123);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
		case 42:
          LocalAmbientSound("melflavpickuprobo/kushiel",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 5:
          LocalAmbientSound("melflavpickuprobo/RocketNailgunLauncher",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 6:
          terminate;
        case 7:
          LocalAmbientSound("melflavpickuprobo/RocketLauncher1",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate; }}
		  
    else if(CheckActorClass(0,"SpacePirate")){ // Mel (Default)
      switch (which){
        case 1:
          LocalAmbientSound("melflavpickup/Pistol",127);    
          Delay(46);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 2:
          LocalAmbientSound("melflavpickup/ZekeShotgun",127);
          Delay(60);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 3:
          LocalAmbientSound("melflavpickup/Crossbow",127);
          Delay(53);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 4:
          LocalAmbientSound("melflavpickup/Ammobox50",127);
          Delay(144);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
		case 42:
          LocalAmbientSound("melflavpickup/kushiel",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 5:
          LocalAmbientSound("melflavpickup/RocketNailgunLauncher",127);
          Delay(69);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 6:
          terminate;
        case 7:
          LocalAmbientSound("melflavpickup/RocketLauncher1",127);
          Delay(69);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate; }}
		  
    else if(CheckActorClass(0,"RoboMel") && GetPlayerInfo(PlayerNumber(),PLAYERINFO_GENDER) == 2){ //Robo Mel TTS
      switch (which){
        case 1:
          LocalAmbientSound("rmelttsflavpickup/Pistol",127);    
          Delay(46);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 2:
          LocalAmbientSound("rmelttsflavpickup/ZekeShotgun",127);
          Delay(60);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 3:
          LocalAmbientSound("rmelttsflavpickup/Crossbow",127);
          Delay(53);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 4:
          LocalAmbientSound("rmelttsflavpickup/Ammobox50",127);
          Delay(144);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
		case 42:
          LocalAmbientSound("rmelttsflavpickup/kushiel",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 5:
          LocalAmbientSound("rmelttsflavpickup/RocketNailgunLauncher",127);
          Delay(69);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 6:
          terminate;
        case 7:
          LocalAmbientSound("rmelttsflavpickup/RocketLauncher1",127);
          Delay(69);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate; }}
		  
    else if(CheckActorClass(0,"RoboMel")){ //Robo Mel (Character)
      switch (which){
        case 1:
          LocalAmbientSound("melflavpickuprobo/Pistol",127);
          Delay(41);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 2:
          LocalAmbientSound("melflavpickuprobo/ZekeShotgun",127);
          Delay(49);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 3:
          LocalAmbientSound("melflavpickuprobo/Crossbow",127);
          Delay(35);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 4:
          LocalAmbientSound("melflavpickuprobo/Ammobox50",127);
          Delay(123);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
		case 42:
          LocalAmbientSound("melflavpickuprobo/kushiel",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 5:
          LocalAmbientSound("melflavpickuprobo/RocketNailgunLauncher",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate;
        case 6:
          terminate;
        case 7:
          LocalAmbientSound("melflavpickuprobo/RocketLauncher1",127);
          Delay(67);
          TakeInventory("PlayingPickupSound",0x7FFFFFFF);
          terminate; }}
    else{
      TakeInventory("PlayingPickupSound",0x7FFFFFFF);
      terminate; }}
}

script "TSPHUDHealthNumberColor" ENTER
{
  if(GetActorProperty( 0, APROP_Health) >= 101){ GiveInventory("Over100Health",1); }
  else{ TakeInventory("Over100Health",1); }
  Delay(6);
  Restart;
}


script "TSPDifficultyLoadouts" ENTER
{
  if (GameSkill() == 0) { GiveInventory("TSPNormalModePickup",1); }
  if (GameSkill() == 1) { GiveInventory("TSPNormalModePickup",1); }
  if (GameSkill() == 2) { GiveInventory("TSPNormalModePickup",1); }
  if (GameSkill() == 3) { GiveInventory("TSPNormalModePickup",1); }
  if (GameSkill() == 4) { GiveInventory("TSPNormalModePickup",1); }
  if (GameSkill() == 5) { GiveInventory("TSPNormalModePickup",1); }
  //if (GameSkill() == 4) { GiveInventory("TSPDTPPickup",1); }
  //if (GameSkill() == 5) { GiveInventory("TSPSurvivorModePickup",1); }
}

script "TSPIDKFAFix" ENTER
{
	if(CheckInventory("HellFireShell") >= 96)
    {
		if(CheckInventory("PoisonShell") >= 96)
		{
				TakeInventory("HellFireShell",96);
				TakeInventory("BuckShotShell",96);
				TakeInventory("PoisonShell",96);
				TakeInventory("ElectricShell",96);
				TakeInventory("TSPShells",96);
				GiveInventory("HellFireShell",20);
				GiveInventory("BuckShotShell",36);
				GiveInventory("PoisonShell",20);
				GiveInventory("ElectricShell",20);
				GiveInventory("TSPShells",96);
				GiveInventory("MelZekeShotgun",1);
				Delay(6);
				Restart;
			}
		}
		Delay(6);
		Restart;
    }

//Shotgun Scripts

script "TSPZekeMessage" (int which)
{
  switch (which){
    case 1:
      hudmessage (s:"[Altfire Again To Cycle Through Ammo Types]";HUDMSG_PLAIN,2,CR_GREEN,1.5,0.375,1.0);
      break;
    case 2:
      hudmessage (s:"[No Alternate Shell Ammo]";HUDMSG_PLAIN,2,CR_GREEN,1.5,0.375,0.42857);
      break;
    case 3:
      hudmessage (s:"[Current Ammo Depleted, Switching To Buckshot]";HUDMSG_PLAIN,2,CR_RED,1.5,0.375,1.5);
      break;
    case 4:
      hudmessage (s:"[Current Ammo Depleted, Switching To Shock Shells]";HUDMSG_PLAIN,2,CR_LIGHTBLUE,1.5,0.375,1.5);
      break;
    case 5:
      hudmessage (s:"[Current Ammo Depleted, Switching To HellFire Shells]";HUDMSG_PLAIN,2,CR_GOLD,1.5,0.375,1.5);
      break;
    case 6:
      hudmessage (s:"[Current Ammo Depleted, Switching To Poison Shells]";HUDMSG_PLAIN,2,CR_DARKGREEN,1.5,0.375,1.5);
      break;
    case 7:
      hudmessage (s:"[Buckshot Shells Selected]";HUDMSG_PLAIN,2,CR_RED,1.5,0.375,0.7142857143);
      break;
    case 8:
      hudmessage (s:"[Shock Shells Selected]";HUDMSG_PLAIN,2,CR_LIGHTBLUE,1.5,0.375,0.7142857143);
      break;
    case 9:
      hudmessage (s:"[HellFire Shells Selected]";HUDMSG_PLAIN,2,CR_GOLD,1.5,0.375,0.7142857143);
      break;
    case 10:
      hudmessage (s:"[Poison Shells Selected]";HUDMSG_PLAIN,2,CR_DARKGREEN,1.5,0.375,0.7142857143);
      break; }
}

script "ShellPickup" (int which, int howmany, int msg)
{
  int shells, maxshells, specshells, maxspecshells, result, giveamt;
  if(!howmany){ howmany = 1; }
  if(CheckInventory("Backpack2") || CheckInventory("Backpack")){ maxshells = 96; }
   else{ maxshells = 48; }
  if(which==4){ maxspecshells = maxshells; }
   else{ maxspecshells = maxshells / 3; }
  if(GetCVar("tsp_shellpool") && which != 4){
    shells = CheckInventory("ElectricShell") + CheckInventory("HellFireShell") + CheckInventory("PoisonShell");
    if(shells < maxshells){ 
      giveamt = maxshells - shells;
      result = 1; }}
  else{
    switch (which){
      case 1:
        specshells = CheckInventory("ElectricShell");
        break;
      case 2:
        specshells = CheckInventory("HellFireShell");
        break;
      case 3:
        specshells = CheckInventory("PoisonShell");
        break;
      case 4:
        specshells = CheckInventory("BuckShotShell");
        break; }
    if(specshells < maxspecshells){ 
      giveamt = maxspecshells - specshells;
      result = 1; }}
  if(result){
    if(howmany < giveamt){ giveamt = howmany; } 
    GiveInventory("TSPShells",giveamt);
    switch (which){
      case 1:
        GiveInventory("ElectricShell",giveamt);
        if(msg){ ShellMessage(1,giveamt); }
        break;
      case 2:
        GiveInventory("HellFireShell",giveamt);
        if(msg){ ShellMessage(2,giveamt); }
        break;
      case 3:
        GiveInventory("PoisonShell",giveamt);
        if(msg){ ShellMessage(3,giveamt); }
        break;
      case 4:
        GiveInventory("BuckShotShell",giveamt);
        if(msg){ ShellMessage(4,giveamt); }
        break; }}
  setresultvalue(result);
}


//Dahlia Scripts

script "BoltPickup" (int which, int howmany, int msg)
{
  int ammo, maxammo, giveamt, result;
  switch (which){
    case 1:
      ammo = CheckInventory("DahliaNormalAmmo");
      if(CheckInventory("Backpack2") || CheckInventory("Backpack")){ maxammo = 60; }
      else{ maxammo = 40; }
      break;
    case 2:
      ammo = CheckInventory("DahliaExplosiveAmmo");
      if(CheckInventory("Backpack2") || CheckInventory("Backpack")){ maxammo = 40; }
      else{ maxammo = 20; }
      break;
    /*case 3:
      ammo = CheckInventory("DahliaNormalAmmo");
      if(CheckInventory("Backpack2") || CheckInventory("Backpack")){ maxammo = 60; }
      else{ maxammo = 40; }
      break;*/ }
  giveamt = maxammo - ammo;
  if(howmany < giveamt){ giveamt = howmany; } 
  if(giveamt > 0){ 
    result = 1;
    switch (which){
      case 1:
        GiveInventory("DahliaNormalAmmo",giveamt);
        if(msg){ BoltMessage(1,giveamt); }
        break;
      case 2:
        GiveInventory("DahliaExplosiveAmmo",giveamt);
        if(msg){ BoltMessage(2,giveamt); }
        break;
      /*case 3:
        GiveInventory("AmmoBoxAmmo",giveamt);
        if(msg){ BoltMessage(3,giveamt); }
        break;*/ }}
  setresultvalue(result);
}

script "TSPBoltStickScript" (void)
{
  int NewTID = UniqueTID();
  Thing_ChangeTID (0,NewTID);
  int BoltAngle = GetActorAngle(0); 
  int BoltX = GetActorZ(0);
  SetActivator(0,AAPTR_TRACER);
  int TracerAngle = GetActorAngle(0);
  int TracerX = GetActorZ(0);
  SetUserVariable(NewTID,"user_height",BoltX - TracerX);
  SetUserVariable(NewTID,"user_angle",FixedAngMod(BoltAngle - TracerAngle));
}

script "TSPBoltExplodeScript" (int which)
{
  int newtid;
  int BoltX, BoltY, BoltZ, BoltZVar, TracerX, TracerY, TracerZ;
  int BoltAngle, TracerAngle;
  //int BoltPitch, TracerPitch;
  newtid = UniqueTID();
  BoltX = GetActorX(0);
  BoltY = GetActorY(0);
  BoltZ = GetActorZ(0);
  BoltZVar = GetUserVariable(0,"user_height");
  BoltAngle = GetActorAngle(0);
  //BoltPitch = GetActorPitch(0);
  if(which == 1){
    SpawnForced("BoltExplodeDeath",BoltX,BoltY,BoltZ,newtid,BoltAngle);
    /* SetActorPitch(newtid,BoltPitch); */}
  else if(which == 2){
    SetActivator(0,AAPTR_TRACER);
    TracerX = GetActorX(0);
    TracerY = GetActorY(0);
    TracerZ = GetActorZ(0);
    TracerAngle = GetActorAngle(0);
    //TracerPitch = GetActorPitch(0);
    SpawnForced("BoltExplodeXDeath",TracerX,TracerY,TracerZ,newtid,TracerAngle);
    /* SetActorPitch(newtid,TracerPitch); */}
  else{
    SetActivator(0,AAPTR_TRACER);
    if(CheckFlag(0,"NORADIUSDMG")){
      Thing_Damage2(0,Random(30,90),"BoltScriptDmg"); }
    else{
      Thing_Damage2(0,Random(128,384),"BoltScriptDmg"); }
    TracerX = GetActorX(0);
    TracerY = GetActorY(0);
    TracerZ = GetActorZ(0);
    TracerAngle = GetActorAngle(0);
    //TracerPitch = GetActorPitch(0);
    SpawnForced("BoltExplodeXDeath",TracerX,TracerY,TracerZ + BoltZVar,newtid,TracerAngle);
    /* SetActorPitch(newtid,TracerPitch); */}
}

//ToolBox Scripts

script "RocketPickup" (int howmany, int msg)
{
  int ammo, maxammo, giveamt, result;
  ammo = CheckInventory("ToolboxAmmo");
  if(CheckInventory("Backpack2") || CheckInventory("Backpack")){ maxammo = 60; }
  else{ maxammo = 30; }
  giveamt = maxammo - ammo;
  if(howmany < giveamt){ giveamt = howmany; } 
  if(giveamt > 0){ 
    result = 1;
    GiveInventory("ToolboxAmmo",giveamt);
    if(msg){ RocketMessage(giveamt); }}
  setresultvalue(result);
}

//Beam and other scripts

script "TSPBeamDeath" (void)
{
  SetActorProperty(0,APROP_RenderStyle,STYLE_Add);
}

Script "PlayerTID" ENTER
{
  int PlayerNumberCheck = PlayerNumber();
  int CurTID = ActivatorTID();
  if(!GArray50[PlayerNumberCheck]  ||  !ActivatorTID() || ThingCount(T_NONE,CurTID) > 1){
    int NewPlayerTID = UniqueTID();
    GArray50[PlayerNumberCheck] = NewPlayerTID;
    Thing_ChangeTid(0,NewPlayerTID); }
  delay(105);
  restart;
}

Script "DProjTID" (void)
{
  int NewTID = UniqueTID();
  SetUserVariable(0,"user_DProjTID",NewTID);
  SetResultValue(NewTID);
}

Script "BeamTID" (void)
{
  int pnum = ActivatorTID();
  SetResultValue(pnum);
}

function int GetToaster(int WhichCVar) //More will be done with this later
{
  int toaster = GetCVar("tsp_toaster");
  return toaster;
}

script "TSPWOGBeamSpawn" (int FiredByPlayer)
{
  int newtid, Position;
  int LastX, LastY, LastZ, LastXFixed, LastYFixed, LastZFixed;
  int beamstyle, toaster;
  int lastcurve;
  int HowClose, DivMapUnit;
  int BezierX, BezierY, BezierAmount;
  int BezierX1, BezierX2, BezierY1, BezierY2;
  int t, Loopx, Loopy, Loopz;
  int tminus, tminussq, tminuscu, tsq, tcu;
  
  int InitialxFixed = GetActorX(0);
  int InitialyFixed = GetActorY(0);
  int InitialzFixed = GetActorZ(0);

  int Initialx = InitialxFixed >> 16;
  int Initialy = InitialyFixed >> 16;
  int Initialz = InitialzFixed >> 16;

  toaster = GetToaster(1);

  if (toaster <= 0){
    HowClose = 1; 
    DivMapUnit = 1; }
  else if (toaster == 1){
    HowClose = 4; 
    DivMapUnit = 1; }
  else{
    HowClose = 6; 
    DivMapUnit = 1; }

  newtid = UniqueTID();
  Thing_ChangeTid(0,newtid);

  SetActivator(0,AAPTR_TARGET);

    /*
  if (ClassifyActor(0) &  ACTOR_PLAYER){ int FiredByPlayer = 1; }


  if (GetCVar("tsp_beamstyle") == 0){ beamstyle = 0; }
  else if (GetCVar("tsp_beamstyle") == 2 && FiredByPlayer){ beamstyle = 1; }
  else if (GetCVar("tsp_beamstyle") == 2){ beamstyle = 2; }
  else { beamstyle = 1; }  */

  if (GetCVar("tsp_beamstyle") == 0){ beamstyle = 0; }
  else if (GetCVar("tsp_beamstyle") == 2){ beamstyle = 2; }
  else { beamstyle = 1; }

  if (FiredByPlayer == 1){
    int DummyProjTID = GetUserVariable(0,"user_DProjTID");
    LastxFixed = GetActorX(DummyProjTID);
    LastyFixed = GetActorY(DummyProjTID);
    LastzFixed = GetActorZ(DummyProjTID); 
    lastcurve = 0; 
    int pnum = PlayerNumber() + 1; }
  else{
    pnum = ActivatorTID();     
    LastxFixed = LastxFixedA[pnum];
    LastyFixed = LastyFixedA[pnum];
    LastzFixed = LastzFixedA[pnum];
    lastcurve = LastCurveA[pnum]; }

  Thing_ChangeTid(newtid,pnum);
  
  Lastx = LastxFixed >> 16;
  Lasty = LastyFixed >> 16;
  Lastz = LastzFixed >> 16;
  
  int InitialAngle = VectorAngle(LastxFixed - InitialxFixed, LastyFixed - InitialyFixed);

  int Diffx = Initialx - Lastx;
  int Diffy = Initialy - Lasty;
  int Diffz = Initialz - Lastz;
  
  int LineLengthInteger = VectorLength(Diffx,Diffy);
  LineLengthInteger = VectorLength(Diffz,LineLengthInteger);

  int LineLengthFixed = LineLengthInteger << 16;

  int xLengthFixed = abs(LastxFixed - InitialxFixed);
  int yLengthFixed = abs(LastyFixed - InitialyFixed);
  int zLengthFixed = abs(LastzFixed - InitialzFixed);

  if (LineLengthInteger == 0){ Terminate; }
  
  if (FiredByPlayer == 1){ BezierAmount = 0.5; }
  else{ BezierAmount = 3.0; }
  
  LineLengthInteger = LineLengthInteger * DivMapUnit;
  
  switch (beamstyle)
  {
    case 0:
      for (Position = 0; Position < LineLengthInteger; Position++){
        t = FixedDiv((Position << 16),(LineLengthInteger << 16));
        if (t < 0){ t =0; }
        tminus = (1.0-t);
        Loopx = ( FixedMul(tminus,LastxFixed) + FixedMul(t,InitialxFixed) );
        Loopy = ( FixedMul(tminus,LastyFixed) + FixedMul(t,InitialyFixed) );
        Loopz = ( FixedMul(tminus,LastzFixed) + FixedMul(t,InitialzFixed) );
        if (Position % HowClose == 0){
          SpawnForced("WOGMissileTrail",Loopx,Loopy,Loopz,0,0); }}
      break;

    case 1:
      while(BezierX == 0 || BezierY == 0){ //still not sure what is causing the zeroing bug, but this workaround works
        if (LastCurve < 0){
          BezierX = random(InitialxFixed,LastxFixed) + FixedMul(xLengthFixed,random(1,BezierAmount));
          BezierY = random(InitialyFixed,LastyFixed) + FixedMul(yLengthFixed,random(1,BezierAmount));
          LastCurve = 1; }
        else if (LastCurve > 0){
          BezierX = random(InitialxFixed,LastxFixed) - FixedMul(xLengthFixed,random(1,BezierAmount));
          BezierY = random(InitialyFixed,LastyFixed) - FixedMul(yLengthFixed,random(1,BezierAmount));
          LastCurve = -1; }
        else{
          LastCurve = random(-1000,1000);
          if (LastCurve <= 0){
            BezierX = random(InitialxFixed,LastxFixed) + FixedMul(xLengthFixed,random(1,BezierAmount));
            BezierY = random(InitialyFixed,LastyFixed) + FixedMul(yLengthFixed,random(1,BezierAmount));
            LastCurve = 1; }
          else if (LastCurve < 0){
            BezierX = random(InitialxFixed,LastxFixed) - FixedMul(xLengthFixed,random(1,BezierAmount));
            BezierY = random(InitialyFixed,LastyFixed) - FixedMul(yLengthFixed,random(1,BezierAmount));
            LastCurve = -1; }}}
      if ((InitialAngle >= 0.125 && InitialAngle <= 0.375) || (InitialAngle >= 0.625 && InitialAngle <= 0.875)){
        for (Position = 0; Position < LineLengthInteger; Position++){
          t = FixedDiv((Position << 16),(LineLengthInteger << 16));
          if (t < 0){ t =0; }
          tminus = (1.0-t);
          tminussq = FixedMul(tminus,tminus);
          tsq = FixedMul(t,t);        
          Loopx = ( FixedMul(tminussq,LastxFixed) + 2 * FixedMul(FixedMul(tminus,t),BezierX) + FixedMul(tsq,InitialxFixed) );
          Loopy = ( FixedMul(tminus,LastyFixed) + FixedMul(t,InitialyFixed) );
          Loopz = ( FixedMul(tminus,LastzFixed) + FixedMul(t,InitialzFixed) );
          if (Position % HowClose == 0){
            SpawnForced("WOGMissileTrail",Loopx,Loopy,Loopz,0,0); }}}
      else{
        for (Position = 0; Position < LineLengthInteger; Position++){
          t = FixedDiv((Position << 16),(LineLengthInteger << 16));
          if (t < 0){ t =0; }
          tminus = (1.0-t);
          tminussq = FixedMul(tminus,tminus);
          tsq = FixedMul(t,t);        
          Loopy = ( FixedMul(tminussq,LastyFixed) + 2 * FixedMul(FixedMul(tminus,t),BezierY) + FixedMul(tsq,InitialyFixed) );
          Loopx = ( FixedMul(tminus,LastxFixed) + FixedMul(t,InitialxFixed) );
          Loopz = ( FixedMul(tminus,LastzFixed) + FixedMul(t,InitialzFixed) );
          if (Position % HowClose == 0){
            SpawnForced("WOGMissileTrail",Loopx,Loopy,Loopz,0,0); }}}
      break;

    case 2:
      while(BezierX1 == 0 || BezierX2 == 0 || BezierY1 == 0 || BezierY2 == 0){ //still not sure what is causing the zeroing bug, but this workaround works
        if (LastCurve < 0){
          BezierX1 = LastxFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierX2 = InitialxFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierY1 = LastyFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierY2 = InitialyFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
          LastCurve = 1; }
        else if (LastCurve > 0){
          BezierX1 = LastxFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierX2 = InitialxFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierY1 = LastyFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
          BezierY2 = InitialyFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
          LastCurve = -1;}
        else{
          LastCurve = random(-1000,1000);
          if (LastCurve <= 0){
            BezierX1 = LastxFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierX2 = InitialxFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierY1 = LastyFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierY2 = InitialyFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
            LastCurve = 1; }
          else if (LastCurve < 0){
            BezierX1 = LastxFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierX2 = InitialxFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierY1 = LastyFixed - random((LineLengthFixed / 8),(LineLengthFixed / 16));
            BezierY2 = InitialyFixed + random((LineLengthFixed / 8),(LineLengthFixed / 16));
            LastCurve = -1; }}}
 
      if ( (InitialAngle >= 0.125 && InitialAngle <= 0.375) || (InitialAngle >= 0.625 && InitialAngle <= 0.875) ){
        for (Position = 0; Position < LineLengthInteger; Position++){
          t = FixedDiv((Position << 16),(LineLengthInteger << 16));
          if (t < 0){ t =0; }
          tminus = (1.0-t);
          tminussq = FixedMul(tminus,tminus);
          tminuscu = FixedMul(tminussq,tminus);    
          tsq = FixedMul(t,t);        
          tcu = FixedMul(tsq,t);
          Loopx = ( FixedMul(tminuscu,LastxFixed) + 3 * FixedMul(tminussq,FixedMul(t,BezierX1)) + 3 * FixedMul(tminus,FixedMul(tsq,BezierX2)) + FixedMul(tcu,InitialxFixed) );
          Loopy = ( FixedMul(tminus,LastyFixed) + FixedMul(t,InitialyFixed) );
          Loopz = ( FixedMul(tminus,LastzFixed) + FixedMul(t,InitialzFixed) );
          if (Position % HowClose == 0){
            SpawnForced("WOGMissileTrail",Loopx,Loopy,Loopz,0,0); }}}
      else{
        for (Position = 0; Position < LineLengthInteger; Position++){
          t = FixedDiv((Position << 16),(LineLengthInteger << 16));
          if (t < 0){ t =0; }
          tminus = (1.0-t);
          tminussq = FixedMul(tminus,tminus);
          tminuscu = FixedMul(tminussq,tminus);    
          tsq = FixedMul(t,t);        
          tcu = FixedMul(tsq,t);
          Loopy = ( FixedMul(tminuscu,LastyFixed) + 3 * FixedMul(tminussq,FixedMul(t,BezierY1)) + 3 * FixedMul(tminus,FixedMul(tsq,BezierY2)) + FixedMul(tcu,InitialyFixed) );
          Loopx = ( FixedMul(tminus,LastxFixed) + FixedMul(t,InitialxFixed) );
          Loopz = ( FixedMul(tminus,LastzFixed) + FixedMul(t,InitialzFixed) );
          if (Position % HowClose == 0){
            SpawnForced("WOGMissileTrail",Loopx,Loopy,Loopz,0,0); }}}
      break;
  }
  
  LastxFixedA[pnum] = Loopx;
  LastyFixedA[pnum] = Loopy; 
  LastzFixedA[pnum] = Loopz; 
  LastCurveA[pnum] = lastcurve;
  setresultvalue(1);
}

script "TSPWOGBeam" (int which)
{
  switch (which){
    case 3:
      SetActivator(0,AAPTR_TRACER);
      if(CheckFlag(0,"ISMONSTER") == FALSE){
        terminate; }
      else if(CheckFlag(0,"BOSS") == TRUE){
        GiveInventory("BossUnTarget", 1);
        Delay(4);
        TakeInventory("BossUnTarget", 1);
        GiveInventory("BossCanTarget", 1);
        terminate; }
      else if(CheckFlag(0,"NOTARGET") == TRUE){
        GiveInventory("BossUnTarget", 1);
        Delay(4);
        TakeInventory("BossUnTarget", 1);
        GiveInventory("BossCanTarget", 1);
        terminate; }
      else{
        GiveInventory("BossUnTarget", 1);
        Delay(1);
        TakeInventory("BossUnTarget", 1);
        GiveInventory("BossCanTarget", 1);
        terminate; }
    case 4:
      SetActorProperty(0,APROP_RenderStyle,STYLE_Add);
      terminate; }
}