from Cohesion import Cohesion
from Complexity import Complexity
from Coupling import Coupling
from FactExtraction import FactExtractor

# Step 1: Extract Model
fact_extractor = FactExtractor("Test_Classes/")
# fact_extractor = FactExtractor("source_files/")
model = fact_extractor.make_model()

# Step 2: Classify

# Test step for fitness calculation
ipc = 0
rfc = 0
tcc = 0
ich = 0
lcom5 = 0
wmc = 0
nom = 0
for c in model:
    rfc += Coupling.get_RFC(c)
    ipc += Coupling.get_ICP(c)
    tcc += Cohesion.get_TCC(c)
    ich += Cohesion.get_ICH(c)
    lcom5 += Cohesion.get_LCOM5(c)
    wmc += Complexity.get_WMC(c)
    nom += Complexity.get_NOM(c)
print(model)

