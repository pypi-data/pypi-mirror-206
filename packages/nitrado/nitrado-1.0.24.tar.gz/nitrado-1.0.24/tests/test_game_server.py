from nitrado import GameServer
from tests.mocked_client import MockedClient


def get_a_game_server() -> GameServer:
    data = {
        "status": "started",
        "last_status_change": 1679636808,
        "must_be_started": True,
        "websocket_token": "415511975144cabef35bbf49eaf0e4b1157677d2",
        "hostsystems": {
            "linux": {
                "hostname": "usla652.nitrado.net",
                "servername": "usla652",
                "status": "online"
            },
            "windows": {
                "hostname": "usla992.nitrado.net",
                "servername": "usla992",
                "status": "online"
            }
        },
        "username": "ni1234567_1",
        "user_id": 123456,
        "service_id": 1,
        "location_id": 3,
        "minecraft_mode": False,
        "ip": "5.62.66.117",
        "ipv6": None,
        "port": 10020,
        "query_port": 10020,
        "rcon_port": 15335,
        "label": "ni",
        "type": "Gameserver",
        "memory": "Standard",
        "memory_mb": 1024,
        "game": "arkxb",
        "game_human": "ARK: Survival Evolved (Xbox One)",
        "game_specific": {
            "path": "/games/ni1234567_1/noftp/arkxb/",
            "update_status": "up_to_date",
            "last_update": "2023-03-06T17:19:51",
            "path_available": True,
            "features": {
                "has_backups": True,
                "has_world_backups": False,
                "has_rcon": False,
                "has_application_server": False,
                "has_container_websocket": False,
                "has_file_browser": False,
                "has_ftp": False,
                "has_expert_mode": True,
                "has_packages": False,
                "has_plugin_system": False,
                "has_restart_message_support": True,
                "has_database": False,
                "has_playermanagement_feature": True,
                "has_curseforge_workshop": False
            },
            "log_files": [
                "arkxb/ShooterGame/Saved/Logs/ShooterGame.log",
                "arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log"
            ],
            "config_files": [],
            "curseforge_customer_settings": None
        },
        "modpacks": {},
        "slots": 20,
        "location": "US",
        "credentials": {
            "ftp": None,
            "mysql": None
        },
        "settings": {
            "config": {
                "server-name": "[US] Flashy Thylacoleo hosted by nitrado.net",
                "admin-password": "QUH0TL3I",
                "server-password": "",
                "player-on-map": "False",
                "disable-pvp": "False",
                "hardcore": "False",
                "crosshair": "False",
                "no-hud": "False",
                "voice-chat": "False",
                "near-chat-only": "False",
                "3rd-person": "False",
                "leave-messages": "False",
                "join-messages": "False",
                "message-of-the-day": "This ARK is hosted by nitrado.net",
                "difficulty-offset": "0.5",
                "motd-duration": "20",
                "disable-structure-decay-pve": "False",
                "allow-flyer-carry-pve": "False",
                "max-structures-in-range": "1300",
                "enable-pvp-gamma": "False",
                "no-tribute-downloads": "False",
                "DayCycleSpeedScale": "1",
                "NightTimeSpeedScale": "1",
                "DayTimeSpeedScale": "1",
                "DinoDamageMultiplier": "1.0",
                "PlayerDamageMultiplier": "1.0",
                "StructureDamageMultiplier": "1.0",
                "PlayerResistanceMultiplier": "1.0",
                "DinoResistanceMultiplier": "1.0",
                "StructureResistanceMultiplier": "1.0",
                "XPMultiplier": "1.0",
                "TamingSpeedMultiplier": "1.0",
                "HarvestAmountMultiplier": "1.0",
                "HarvestHealthMultiplier": "1.0",
                "PlayerCharacterWaterDrainMultiplier": "1.0",
                "PlayerCharacterFoodDrainMultiplier": "1.0",
                "DinoCharacterFoodDrainMultiplier": "1.0",
                "PlayerCharacterStaminaDrainMultiplier": "1.0",
                "DinoCharacterStaminaDrainMultiplier": "1.0",
                "PlayerCharacterHealthRecoveryMultiplier": "1.0",
                "DinoCharacterHealthRecoveryMultiplier": "1.0",
                "DinoCountMultiplier": "1.0",
                "PvEStructureDecayPeriodMultiplier": "1.0",
                "ResourcesRespawnPeriodMultiplier": "1.0",
                "ClampResourceHarvestDamage": "False",
                "map": "preinstalled,1,TheIsland",
                "restart-countdown-seconds": "300",
                "active-mods": "",
                "start-with-backup": "",
                "players-join-no-check-list": "",
                "ban-list": "2533274826773268,\n2533274821865701,",
                "prevent-download-survivors": "False",
                "prevent-download-items": "False",
                "prevent-download-dinos": "False",
                "admin-list": "",
                "default-map": "True",
                "map-mod-id": "",
                "active-total-conversion": "",
                "DisableDeathSpectator": "False",
                "OnlyAdminRejoinAsSpectator": "False",
                "BattleNumOfTribesToStartGame": "15",
                "TimeToCollapseROD": "9000",
                "BattleAutoStartGameInterval": "60.000000",
                "BattleAutoRestartGameInterval": "45.000000",
                "BattleSuddenDeathInterval": "300.000000",
                "StructureDestructionTag": "False",
                "ForceRespawnDinos": "False",
                "BanListURL": "",
                "AutoSavePeriodMinutes": "30.000000",
                "activateAdminLogs": "True",
                "gameLogBuffer": "600",
                "map-expert": "",
                "DisableDinoDecayPvE": "False",
                "PvEDinoDecayPeriodMultiplier": "1.0",
                "DisablePvEGamma": "False",
                "exlusivejoin": "False",
                "PlayersExclusiveJoinList": "",
                "ForceAllStructureLocking": "False",
                "AutoDestroyOldStructuresMultiplier": "1.0",
                "bJoinNotifications": "False",
                "bShowStatusNotificationMessages": "False",
                "PerPlatformMaxStructuresMultiplier": "1.0",
                "SpectatorPassword": "",
                "AllowCaveBuildingPvE": "False",
                "nofishloot": "False",
                "DisableDinoRiding": "False",
                "DisableDinoTaming": "False",
                "MaxPersonalTamedDinos": "250",
                "OnlyDecayUnsnappedCoreStructures": "False",
                "TributeItemExpirationSeconds": "86400",
                "TributeDinoExpirationSeconds": "86400",
                "TributeCharacterExpirationSeconds": "86400",
                "current-admin-password": "564266",
                "activateAdminTribeLogs": "True",
                "TribeNameChangeCooldown": "15",
                "AllowHideDamageSourceFromLogs": "False",
                "RandomSupplyCratePoints": "False",
                "DisableWeatherFog": "True",
                "AdminLogging": "False",
                "bForceCanRideFliers": "False",
                "AllowTekSuitPowersInGenesis": "False",
                "EnableCryoSicknessPVE": "False",
                "CryopodNerfDuration": "1",
                "CryopodNerfDamageMult": "1",
                "ItemStackSizeMultiplier": "1.0",
                "AllowCaveBuildingPvP": "False"
            },
            "gameini": {
                "DinoSpawnWeightMultipliers": "",
                "OverrideEngramEntries": "",
                "LevelExperienceRampOverrides": "LevelExperienceRampOverrides=\r\nLevelExperienceRampOverrides=\r\n",
                "OverridePlayerLevelEngramPoints": "",
                "TamedDinoClassDamageMultipliers": "",
                "TamedDinoClassResistanceMultipliers": "",
                "ExcludeItemIndices": "",
                "HarvestResourceItemAmountClassMultipliers": "",
                "OverrideNamedEngramEntries": "",
                "bOnlyAllowSpecifiedEngrams": "bOnlyAllowSpecifiedEngrams=False",
                "GlobalSpoilingTimeMultiplier": "GlobalSpoilingTimeMultiplier=0",
                "GlobalItemDecompositionTimeMultiplier": "GlobalItemDecompositionTimeMultiplier=0",
                "GlobalCorpseDecompositionTimeMultiplier": "GlobalCorpseDecompositionTimeMultiplier=0",
                "OverrideMaxExperiencePointsPlayer": "",
                "OverrideMaxExperiencePointsDino": "",
                "PvPZoneStructureDamageMultiplier": "PvPZoneStructureDamageMultiplier=6.0",
                "bPvEDisableFriendlyFire": "bPvEDisableFriendlyFire=False",
                "ResourceNoReplenishRadiusPlayers": "ResourceNoReplenishRadiusPlayers=1",
                "ResourceNoReplenishRadiusStructures": "ResourceNoReplenishRadiusStructures=1",
                "bAutoPvETimer": "bAutoPvETimer=False",
                "bAutoPvEUseSystemTime": "bAutoPvEUseSystemTime=False",
                "AutoPvEStartTimeSeconds": "AutoPvEStartTimeSeconds=0",
                "AutoPvEStopTimeSeconds": "AutoPvEStopTimeSeconds=0",
                "LayEggIntervalMultiplier": "LayEggIntervalMultiplier=1.0",
                "DinoTurretDamageMultiplier": "DinoTurretDamageMultiplier=1.0",
                "bDisableLootCrates": "bDisableLootCrates=False",
                "DinoHarvestingDamageMultiplier": "DinoHarvestingDamageMultiplier=3.0",
                "bDisableFriendlyFire": "bDisableFriendlyFire=False",
                "CustomRecipeEffectivenessMultiplier": "CustomRecipeEffectivenessMultiplier=1.0",
                "CustomRecipeSkillMultiplier": "CustomRecipeSkillMultiplier=1.0",
                "MatingIntervalMultiplier": "MatingIntervalMultiplier=1.0",
                "EggHatchSpeedMultiplier": "EggHatchSpeedMultiplier=1.0",
                "BabyMatureSpeedMultiplier": "BabyMatureSpeedMultiplier=1.0",
                "bPassiveDefensesDamageRiderlessDinos": "bPassiveDefensesDamageRiderlessDinos=False",
                "KillXPMultiplier": "KillXPMultiplier=1.0",
                "HarvestXPMultiplier": "HarvestXPMultiplier=1.0",
                "CraftXPMultiplier": "CraftXPMultiplier=1.0",
                "GenericXPMultiplier": "GenericXPMultiplier=1.0",
                "SpecialXPMultiplier": "SpecialXPMultiplier=1.0",
                "PGMapName": "PGMapName=PGMap",
                "PGTerrainPropertiesString": "PGTerrainPropertiesString=",
                "ConfigOverrideSupplyCrateItems": "",
                "bDisableDinoRiding": "bDisableDinoRiding=False",
                "bDisableDinoTaming": "bDisableDinoTaming=False",
                "bUseCorpseLocator": "bUseCorpseLocator=False",
                "bDisableStructurePlacementCollision": "bDisableStructurePlacementCollision=False",
                "FastDecayInterval": "FastDecayInterval=43200",
                "bUseSingleplayerSettings": "bUseSingleplayerSettings=False",
                "bAllowUnlimitedRespecs": "bAllowUnlimitedRespecs=False",
                "SupplyCrateLootQualityMultiplier": "SupplyCrateLootQualityMultiplier=1.0",
                "FishingLootQualityMultiplier": "FishingLootQualityMultiplier=1.0",
                "PerLevelStatsMultiplier": "",
                "BabyCuddleIntervalMultiplier": "BabyCuddleIntervalMultiplier=1.0",
                "BabyCuddleGracePeriodMultiplier": "BabyCuddleGracePeriodMultiplier=1.0",
                "BabyCuddleLoseImprintQualitySpeedMultiplier": "BabyCuddleLoseImprintQualitySpeedMultiplier=1.0",
                "BabyImprintingStatScaleMultiplier": "BabyImprintingStatScaleMultiplier=1.0",
                "PlayerHarvestingDamageMultiplier": "PlayerHarvestingDamageMultiplier=1.0",
                "CropGrowthSpeedMultiplier": "CropGrowthSpeedMultiplier=1.0",
                "BabyFoodConsumptionSpeedMultiplier": "BabyFoodConsumptionSpeedMultiplier=1.0",
                "DinoClassDamageMultipliers": "",
                "bPvEAllowTribeWar": "bPvEAllowTribeWar=False",
                "bPvEAllowTribeWarCancel": "bPvEAllowTribeWarCancel=False",
                "CropDecaySpeedMultiplier": "CropDecaySpeedMultiplier=1.0",
                "HairGrowthSpeedMultiplier": "HairGrowthSpeedMultiplier=1.0",
                "FuelConsumptionIntervalMultiplier": "FuelConsumptionIntervalMultiplier=1.313000",
                "KickIdlePlayersPeriod": "KickIdlePlayersPeriod=3600",
                "MaxNumberOfPlayersInTribe": "MaxNumberOfPlayersInTribe=0",
                "UseCorpseLifeSpanMultiplier": "UseCorpseLifeSpanMultiplier=1",
                "GlobalPoweredBatteryDurabilityDecreasePerSecond": "GlobalPoweredBatteryDurabilityDecreasePerSecond=4",
                "bLimitTurretsInRange": "bLimitTurretsInRange=False",
                "LimitTurretsRange": "LimitTurretsRange=10000",
                "LimitTurretsNum": "LimitTurretsNum=100",
                "bHardLimitTurretsInRange": "bHardLimitTurretsInRange=False",
                "bShowCreativeMode": "bShowCreativeMode=False",
                "PreventOfflinePvPConnectionInvincibleInterval": "PreventOfflinePvPConnectionInvincibleInterval=5",
                "TamedDinoCharacterFoodDrainMultiplier": "TamedDinoCharacterFoodDrainMultiplier=1",
                "WildDinoCharacterFoodDrainMultiplier": "WildDinoCharacterFoodDrainMultiplier=1",
                "WildDinoTorporDrainMultiplier": "WildDinoTorporDrainMultiplier=1",
                "PassiveTameIntervalMultiplier": "PassiveTameIntervalMultiplier=1",
                "TamedDinoTorporDrainMultiplier": "TamedDinoTorporDrainMultiplier=1",
                "bIgnoreStructuresPreventionVolumes": "bIgnoreStructuresPreventionVolumes=True",
                "bGenesisUseStructuresPreventionVolumes": "False",
                "bDisableGenesisMissions": "False",
                "BabyImprintAmountMultiplier": "BabyImprintAmountMultiplier=1.0",
                "HexagonRewardMultiplier": "HexagonRewardMultiplier=1",
                "bAllowFlyerSpeedLeveling": "bAllowFlyerSpeedLeveling=False",
                "PreventTransferForClassNames": ""
            },
            "features": {
                "engine-settings": "False"
            },
            "append": {
                "gameini": ""
            },
            "general": {
                "expertMode": "True",
                "battleye": "True",
                "server-language": "en",
                "vday": "False",
                "mod-update-list": "[]",
                "mod-status-list": "{}",
                "gameplay-log": "False",
                "force-allow-cave-flyers": "True",
                "vac": "True",
                "gamesettings_saved_utc_timestamp_hidden": "1679123222",
                "automatic-update-mechanism": "AUTOMATIC_UPDATE_ON_RESTART",
                "clusterid": "CuDyawB42FxmeZoLQ+64CreomyCouLzmD+wnWNUHx7k=",
                "enablecluster": "True",
                "PrimitivePlus": "False",
                "enable-idle-player-kick": "False",
                "no-anti-speed-hack": "False",
                "no-biome-walls": "False",
                "notify-admin-commands-in-chat": "False",
                "metrics": "False",
                "CrossPlay": "True",
                "ActiveEvent": "WinterWonderland",
                "structurememopts": "True",
                "noundermeshchecking": "False",
                "noundermeshkilling": "False",
                "NewYearEvent": "True",
                "useitemdupecheck": "True"
            },
            "start-param": {
                "PvPStructureDecay": "True",
                "PreventOfflinePvP": "False",
                "PreventOfflinePvPInterval": "800",
                "ShowFloatingDamageText": "False",
                "DisableImprintDinoBuff": "False",
                "AllowAnyoneBabyImprintCuddle": "True",
                "OverideStructurePlatformPrevention": "True",
                "EnableExtraStructurePreventionVolumes": "False",
                "NonPermanentDiseases": "True",
                "PreventDiseases": "True",
                "OverrideStructurePlatformPrevention": "False",
                "PreventTribeAlliances": "False",
                "AllowRaidDinoFeeding": "True",
                "AllowHitMarkers": "True",
                "FastDecayUnsnappedCoreStructures": "True",
                "TribeLogDestroyedEnemyStructures": "True",
                "OverrideOfficialDifficulty": "0",
                "PreventDownloadSurvivors": "False",
                "PreventDownloadItems": "False",
                "PreventDownloadDinos": "False",
                "PreventUploadSurvivors": "False",
                "PreventUploadItems": "False",
                "PreventUploadDinos": "False",
                "ForceFlyerExplosives": "True",
                "DestroyUnconnectedWaterPipes": "True",
                "PvPDinoDecay": "True",
                "PvEAllowStructuresAtSupplyDrops": "False",
                "AllowCrateSpawnsOnTopOfStructures": "False",
                "UseOptimizedHarvestingHealth": "True",
                "ClampItemSpoilingTimes": "True",
                "AutoDestroyDecayedDinos": "False",
                "AllowFlyingStaminaRecovery": "False",
                "AllowMultipleAttachedC4": "False",
                "bAllowPlatformSaddleMultiFloors": "False",
                "PreventSpawnAnimations": "True",
                "AutoDestroyStructures": "False",
                "MinimumDinoReuploadInterval": "0",
                "OnlyAutoDestroyCoreStructures": "True",
                "OxygenSwimSpeedStatMultiplier": "1.0",
                "ServerAutoForceRespawnWildDinosInterval": "0",
                "CrossARKAllowForeignDinoDownloads": "False",
                "ClampItemStats": "True",
                "EnableCryopodNerf": "False",
                "NewYear1UTC": "",
                "NewYear2UTC": ""
            }
        },
        "quota": None,
        "query": {
            "server_name": "[US]- EPIX ARK -Isl1-20x/6Man/FRESHWIPE/MaxWild150/CusDrop?",
            "connect_ip": "5.62.66.117:10020",
            "map": "TheIsland",
            "version": "959.4",
            "player_current": 0,
            "player_max": 20,
            "players": []
        }
    }
    return GameServer(**data)


def test_game_server():
    game_server = get_a_game_server()
    assert game_server.service_id == 1
    assert game_server.status == 'started'
    assert game_server.user_id == 123456
    assert game_server.slots == 20
    assert game_server.query['server_name'] == '[US]- EPIX ARK -Isl1-20x/6Man/FRESHWIPE/MaxWild150/CusDrop?'

