from coffea.util import load, save
from coffea.processor import accumulate


if __name__ == "__main__":
    
    data_paths = [
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_C0/hists_DY_sfl_data_Prompt25_2025_DY_sfl_C0.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_C1/hists_DY_sfl_data_Prompt25_2025_DY_sfl_C1.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_D/hists_DY_sfl_data_Prompt25_2025_DY_sfl_D.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_E/hists_DY_sfl_data_Prompt25_2025_DY_sfl_E.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_F0/hists_DY_sfl_data_Prompt25_2025_DY_sfl_F0.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_F1/hists_DY_sfl_data_Prompt25_2025_DY_sfl_F1.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_G0/hists_DY_sfl_data_Prompt25_2025_DY_sfl_G0.coffea",
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl_G1/hists_DY_sfl_data_Prompt25_2025_DY_sfl_G1.coffea",
    ]

    combined = accumulate([load(path) for path in data_paths])

    save(
        combined,
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl/"
        "hists_DY_sfl_data_Prompt25_2025_DY_sfl.coffea",
    )
