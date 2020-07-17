import ROOT
ROOT.EnableImplicitMT()

f = ROOT.TFile("./rootfiles/signal.root", "OPEN")
tree = f.Get("mumu")
tree.Print()

df = ROOT.RDataFrame("mumu", "./rootfiles/signal.root")
evtCount = df.Count()
print("Original number of events/entries in the tree: ", evtCount.GetValue())
