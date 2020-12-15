


import openmc
import pytest


def test_inf_media():
    # setup and infinite media problem
    model = openmc.model.Model()

    # create a material
    mat = openmc.Material()
    mat.add_nuclide('C12', 1.0, 'ao')

    cell = openmc.Cell(fill=mat)
    cell.region = openmc.rectangular_prism(1E5, 1E5, boundary_type='reflective')

    model.materials = [mat]
    model.geometry = openmc.Geometry([cell])
    model.settings.run_mode = 'fixed source'
    model.settings.particles = 10000
    model.settings.batches = 10

    model.export_to_xml()

    openmc.run()

