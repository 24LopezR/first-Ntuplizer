import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("demo")
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.Services_cff')

# Debug printout and summary.
process.load("FWCore.MessageService.MessageLogger_cfi")

from Configuration.AlCa.GlobalTag import GlobalTag

# Select number of events to be processed
nEvents = 200
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(nEvents) )

cwd = os.getcwd()
# Read events
listOfFiles = [f'file:../../../output_GS_500mm_SlavaFix.root']
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( listOfFiles ),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents = cms.untracked.uint32(0)
  )
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_v7')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printTree = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(0),
  printVertex = cms.untracked.bool(False),
  printOnlyHardInteraction = cms.untracked.bool(False), # Print only status=3 particles. This will not work for Pythia8, which does not have any such particles.
  src = cms.InputTag("genParticles")
)

## Define the process to run 
## 
process.load("Analysis.Muon-Ntuplizer.DisplacedSUSY_GENSIM_ntuples_cfi")
process.ntuples.nameOfOutput = 'Ntuples_GENSIM_SMuonToMuGravitino_500_500mm_SlavaFix.root'
process.p = cms.EndPath(process.printTree + process.ntuples)
