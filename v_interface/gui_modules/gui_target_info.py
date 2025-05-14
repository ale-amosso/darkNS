def get_target_info(target, dm_mass, targets, u):
    if target == "electron":
        heavy_dm = dm_mass.calc_rel_heavy_dm_mass(target)
        v_heavy_dm = dm_mass.calc_rel_very_heavy_dm_mass(target)
        light_dm = dm_mass.calc_rel_light_dm_mass(target)
        v_light_dm = dm_mass.calc_rel_very_light_dm_mass(target)
        density = targets.calc_density(target)

        electron_text = ("Electron is relativistic and the cross section will be calculated later.\n \n"
                         +
                         "Electron density is " + str(u.format_quantity(density))

                         + "\n\nHeavy dark matter: the value of the DM mass is:\n "
                         + str(u.format_quantity(heavy_dm[0])) + " GeV"
                         + " << mχ <<"
                         + str(u.format_quantity(heavy_dm[1])) + " GeV \n\n"

                         + "Very heavy dark matter: the value of the DM mass is:\n "
                         + "mχ >>" + str(u.format_quantity(v_heavy_dm[0])) + " GeV \n\n"

                         + "Light dark matter: the value of the DM mass is:\n "
                         + str(u.format_quantity(light_dm[0])) + " GeV"
                         + " << mχ <<"
                         + str(u.format_quantity(light_dm[1])) + " GeV \n\n"

                         + "Very Light dark matter: the value of the DM mass is:\n "
                         + "mχ <<"
                         + str(u.format_quantity(v_light_dm[1])) + " GeV")

        return electron_text
    elif target == "neutron":
        heavy_dm = dm_mass.calc_non_rel_heavy_dm_mass(target)
        v_heavy_dm = dm_mass.calc_non_rel_very_heavy_dm_mass(target)
        light_dm = dm_mass.calc_non_rel_light_dm_mass(target)
        density = targets.calc_density(target)
        volume_F = targets.calc_F_volume(target)
        delta_t = targets.calc_delta_t()

        neutron_text = ("Neutron is non-relativistic.\n \n"
                        +
                        "Neutron density is " + str(u.format_quantity(density))
                        +
                        "\n \nNeutron Fermi Volume is " + str(u.format_quantity(volume_F))
                        +
                        "\n \nDelta_t is  " + str(u.format_quantity(delta_t))
                        + "\n"
                        + "Light dark matter: the value of the DM mass is:\n "
                        + str(u.format_quantity(light_dm[0])) + " GeV"
                        + " << mχ "
                        + "\n\nHeavy dark matter: the value of the DM mass is:\n "
                        + str(u.format_quantity(heavy_dm[0])) + " GeV"
                        + " << mχ <<"
                        + str(u.format_quantity(heavy_dm[1])) + " GeV \n\n"

                        + "Very heavy dark matter: the value of the DM mass is:\n "
                        + "mχ >>" + str(u.format_quantity(v_heavy_dm[0])) + " GeV \n\n"
                        + "\n\n")

        return neutron_text
    else:
        #cs = nr_cross_section.cross_section_thres_nr(target)
        #formatted_cs = u.format_quantity(cs)
        return target.capitalize() + " is relativistic and the threshold cross section is: " #+ str(formatted_cs)
