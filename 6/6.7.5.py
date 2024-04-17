import ch06_12_DualMomentum

dm = ch06_12_DualMomentum.DualMomentum()
rm = dm.get_rltv_momentum('2023-07-01', '2023-12-31', 10)
dm.get_abs_momentum(rm, '2024-01-01', '2024-04-15')