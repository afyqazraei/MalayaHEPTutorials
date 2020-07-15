import ROOT, glob, os, sys

varList = [
          "evtWeight",
            "evtWeight_Final",
              "passMassVCand",
                "passDeepTagWMD2p5HP",
                  "passDeepTagWMD1p0HP",
                    "passDeepTagWMD0p5HP",
                      "passDeepTagWMDCR", 
                        "passTau21HP",
                          "passTau21LP",  
                            "ZVCand_mass",
                              "ZCand_pt",
                                "VCand_pt",
                                  "VCand_mass_tag",
                                    "VCand_deepTagMD_WvsQCD",
                                      "ZCand_eta",
                                        "ZCand_phi",
                                          "ZCand_mass",
                                            "ZCand_lep1etaSC",
                                              "VCand_phi",
                                                "VCand_mass",
                                                  ]

files = [x for x in glob.glob("*root")]

for ifile in files:
    treeList = []
    f = ROOT.TFile(ifile, "OPEN")
    
    for br in ["elel", "mumu"]:
        tree = f.Get(br)
        tree.SetBranchStatus("*", 0)
        
        for var in varList:
            tree.SetBranchStatus(var, 1)

        treeList.append(tree.Clone(br+"_clone"))
        print(treeList)

    outFileName = "new_" + ifile
    f.Close()
    f = ROOT.TFile(outFileName, "RECREATE")
    for j in treeList:
        clone = j.CloneTree(-1, "fast")
        clone.Write()



