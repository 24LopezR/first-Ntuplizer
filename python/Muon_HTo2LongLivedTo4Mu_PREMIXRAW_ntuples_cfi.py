import FWCore.ParameterSet.Config as cms

ntuples = cms.EDAnalyzer('ntuplizer',
    nameOfOutput = cms.string('NTuples_fromGENSIM_v0.root'),
    isData                        = cms.bool(False),
    EventInfo                     = cms.InputTag("generator"),
    RunInfo                       = cms.InputTag("generator"),
    #muonCollection                = cms.InputTag("muons"),
    TrackerHitsPixelBarrelHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof","SIM"),
    TrackerHitsPixelBarrelLowTofCollection  = cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof","SIM"),
    TrackerHitsPixelEndcapHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof","SIM"),
    TrackerHitsPixelEndcapLowTofCollection  = cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof","SIM"),
    TrackerHitsTECHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsTECHighTof", "SIM"),
    TrackerHitsTECLowTofCollection = cms.InputTag("g4SimHits","TrackerHitsTECLowTof" , "SIM"),
    TrackerHitsTIBHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsTIBHighTof", "SIM"),
    TrackerHitsTIBLowTofCollection = cms.InputTag("g4SimHits","TrackerHitsTIBLowTof" , "SIM"),
    TrackerHitsTIDHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsTIDHighTof", "SIM"),
    TrackerHitsTIDLowTofCollection = cms.InputTag("g4SimHits","TrackerHitsTIDLowTof" , "SIM"),
    TrackerHitsTOBHighTofCollection = cms.InputTag("g4SimHits","TrackerHitsTOBHighTof", "SIM"),
    TrackerHitsTOBLowTofCollection = cms.InputTag("g4SimHits","TrackerHitsTOBLowTof" , "SIM"),

    genParticleCollection         = cms.InputTag("genParticles","","HLT"),
    SimTrackCollection            = cms.InputTag("g4SimHits","","SIM"),
    #bits       = cms.InputTag("TriggerResults","","HLT"),
)