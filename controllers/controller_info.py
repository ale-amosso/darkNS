# _____________________________________________________
# Hey there! This is not being used anymore!
#______________________________________________________


#from functions.target_info import get_target_calculations




#def get_target_info(target, dm_mass, targets, u):
#    """Get data from the model and generate the formatted text for the GUI."""
#    data = get_target_calculations(target, dm_mass, targets)

#    if not data:
#        return f"{target.capitalize()} is relativistic and the threshold cross section is: "

#    if target == "electron":
#        return (f"Electron is relativistic and the cross section will be calculated later.\n \n"
#                f"Electron density is {u.format_quantity(data['density'])}\n\n"
#                f"Heavy dark matter: the value of the DM mass is:\n "
#                f"{u.format_quantity(data['heavy_dm'][0])} GeV << mχ << {u.format_quantity(data['heavy_dm'][1])} GeV\n\n"
#                f"Very heavy dark matter: the value of the DM mass is:\n "
#                f"mχ >> {u.format_quantity(data['v_heavy_dm'][0])} GeV\n\n"
#                f"Light dark matter: the value of the DM mass is:\n "
#                f"{u.format_quantity(data['light_dm'][0])} GeV << mχ << {u.format_quantity(data['light_dm'][1])} GeV\n\n"
#                f"Very Light dark matter: the value of the DM mass is:\n "
#                f"mχ << {u.format_quantity(data['v_light_dm'][1])} GeV")

#    elif target == "neutron":
#        return (f"Neutron is non-relativistic.\n \n"
#                f"Neutron density is {u.format_quantity(data['density'])}\n \n"
#                f"Neutron Fermi Volume is {u.format_quantity(data['volume_F'])}\n \n"
#                f"Delta_t is {u.format_quantity(data['delta_t'])}\n"
#                f"Light dark matter: the value of the DM mass is:\n "
#                f"{u.format_quantity(data['light_dm'][0])} GeV << mχ\n\n"
#                f"Heavy dark matter: the value of the DM mass is:\n "
#                f"{u.format_quantity(data['heavy_dm'][0])} GeV << mχ << {u.format_quantity(data['heavy_dm'][1])} GeV\n\n"
#                f"Very heavy dark matter: the value of the DM mass is:\n "
#                f"mχ >> {u.format_quantity(data['v_heavy_dm'][0])} GeV\n\n")
