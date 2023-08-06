from RSTAB.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RSTAB.enums import MemberRotationalRestraintContinousBeamEffect, MemberRotationalRestraintRotationalStiffness, MemberRotationalRestraintSheetingPosition, MemberRotationalRestraintType

class MemberRotationalRestraint():

    def __init__(self) -> None:
        pass

    @staticmethod
    def Continuous(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        sheeting_material: str = 'S235',
        sheeting_name: str = 'Arval (-) 35/207 - 0.63 (b: 1) | DIN 18807 | Arval',
        position_of_sheeting = MemberRotationalRestraintSheetingPosition.SHEETING_POSITION_POSITIVE,
        continuous_beam_effect = MemberRotationalRestraintContinousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL,
        section_deformation_cdb: bool = True,
        modulus_of_elasticity: float = 205000000000.0,
        sheeting_thickness: float = 0.00063,
        sheeting_moment_of_inertia: float = 7.5e-08,
        sheeting_distance_of_ribs: float = 0.207,
        width_of_sheeting_flange: float = 0.106,
        spring_stiffness: float = 5200.0,
        beam_spacing: float= 3.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Rotational Restraint Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            sheeting_material (str): Sheeting Material
            sheeting_name (str): Sheeting Material
            position_of_sheeting (enum): Position of Sheeting Enumeration
            continuous_beam_effect (enum): Continous Beam Effect Enumeration
            section_deformation_cdb (bool): Section Deformation Cdb Option
            modulus_of_elasticity (float): Modulus of Elasticity
            sheeting_thickness (float): Sheeting Thickness
            sheeting_moment_of_inertia (float): Sheeting Moment of Inertia
            sheeting_distance_of_ribs (float): Sheeting Distance of Ribs
            width_of_sheeting_flange (float): Width of Sheeting Flange
            spring_stiffness (float): Spring Stiffness
            beam_spacing (float): Beam Spacing
            comment (str, optional): Comment
            params (dict, optional): Parameters
        """

        # Client Model | Member Rotational Restraint
        clientObject = Model.clientModel.factory.create('ns0:member_rotational_restraint')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Rotational Restraint No.
        clientObject.no = no

        # Member Rotational Restraint User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Rotational Restraints Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Rotational Restraint Definition Type
        clientObject.type = MemberRotationalRestraintType.TYPE_CONTINUOUS.name

        # Member Rotational Restraint Sheeting Material Name
        clientObject.material_name = sheeting_material

        # Member Rotational Restraint Sheeting Name
        clientObject.sheeting_name = sheeting_name

        # Member Rotational Restraint Position of Sheeting
        clientObject.position_of_sheeting = position_of_sheeting.name

        # Member Rotational Restraint Continuous Beam Effect
        clientObject.continuous_beam_effect = continuous_beam_effect.name

        # Member Rotational Restraint Section Deformation Cdb
        clientObject.section_deformation_cdb = section_deformation_cdb

        # Member Rotational Restraint Modulus of Elasticity
        clientObject.modulus_of_elasticity = modulus_of_elasticity

        # Member Rotational Restraint Sheeting Thickness
        clientObject.sheeting_thickness = sheeting_thickness

        # Member Rotational Restraint Sheeting Moment of Inertia
        clientObject.sheeting_moment_of_inertia = sheeting_moment_of_inertia

        # Member Rotational Restraint Sheeting Distance of Ribs
        clientObject.sheeting_distance_of_ribs = sheeting_distance_of_ribs

        # Member Rotational Restraint Width of Sheeting Flange
        clientObject.width_of_section_flange = width_of_sheeting_flange

        # Member Rotational Restraint Spring Stiffness
        clientObject.spring_stiffness = spring_stiffness

        # Member Rotational Restraint Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Rotational Restraint to client model
        Model.clientModel.service.set_member_rotational_restraint(clientObject)

    @staticmethod
    def Discrete(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        section_material: str = 'S235',
        section_name: str = 'CHC 60.3x3.2',
        rotational_stifness: list = [MemberRotationalRestraintRotationalStiffness.ROTATIONAL_STIFFNESS_INFINITELY],
        continous_beam_effect = MemberRotationalRestraintContinousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL,
        section_deformation_cdb: bool =  True,
        modulus_of_elasticity: float = 205000000000.0,
        section_moment_of_inertia: float = 2.35e-07,
        purlin_spacing: float = 1.0,
        beam_spacing: float = 3.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Rotational Restraint Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            section_material (str): Section Material
            section_name (str): Section Name
            rotational_stifness (list): Rotational Stiffness
                if rotational_stiffness[0] == MemberRotationalRestraintRotationalStiffness.ROTATIONAL_STIFFNESS_INFINITELY:
                    pass
                elif rotational_stiffness[0] == MemberRotationalRestraintRotationalStiffness.ROTATIONAL_STIFFNESS_MANUALLY:
                    rotational_stiffness[1] = rotational_stiffness_value
            continous_beam_effect (enum): Continous Beam Effect Enumeration
            section_deformation_cdb (bool): Section Deformation Cdb Option
            modulus_of_elasticity (float): Modulus of Elasticity
            section_moment_of_inertia (float): Section Moment of Inertia
            purlin_spacing (float): Purlin Spacing
            beam_spacing (float): Beam Spacing
            comment (str, optional): Comment
            params (dict, optional): Params
        """

        # Client Model | Member Rotational Restraint
        clientObject = Model.clientModel.factory.create('ns0:member_rotational_restraint')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Rotational Restraint No.
        clientObject.no = no

        # Member Rotational Restraint User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Rotational Restraints Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Rotational Restraint Definition Type
        clientObject.type = MemberRotationalRestraintType.TYPE_DISCRETE.name

        # Member Rotational Restraint Section Material Name
        clientObject.material_name = section_material

        # Member Rotational Restraint Section Name
        clientObject.section_name = section_name

        # Member Rotational Restraint Stiffness Cda
        clientObject.rotational_stiffness = rotational_stifness[0].name
        if rotational_stifness[0].name == MemberRotationalRestraintRotationalStiffness.ROTATIONAL_STIFFNESS_MANUALLY.name:
            clientObject.rotational_stiffness_value = rotational_stifness[1]

        # Member Rotational Restraint Continuous Beam Effect
        clientObject.continuous_beam_effect = continous_beam_effect.name

        # Member Rotational Restraint Section Deformation Cdb
        clientObject.section_deformation_cdb = section_deformation_cdb

        # Member Rotational Restraint Modulus of Elasticity
        clientObject.modulus_of_elasticity = modulus_of_elasticity

        # Member Rotational Restraint Section Moment of Inertia
        clientObject.section_moment_of_inertia = section_moment_of_inertia

        # Member Rotational Restraint Purlin Spacing
        clientObject.purlin_spacing = purlin_spacing

        # Member Rotational Restraint Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Rotational Restraint to client model
        Model.clientModel.service.set_member_rotational_restraint(clientObject)

    @staticmethod
    def Manually(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        rotational_spring_stiffness: float = 3000.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Rotational Restraint Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            rotational_spring_stiffness (float): Rotational Spring Stiffness
            comment (str, optional): Comment
            params (dict, optional): Params
        """

        # Client Model | Member Rotational Restraint
        clientObject = Model.clientModel.factory.create('ns0:member_rotational_restraint')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Rotational Restraint No.
        clientObject.no = no

        # Member Rotational Restraint User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Rotational Restraints Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Rotational Restraint Definition Type
        clientObject.type = MemberRotationalRestraintType.TYPE_MANUALLY.name

        # Member Rotational Restraint Total Rotational Spring Stiffness
        clientObject.total_rotational_spring_stiffness = rotational_spring_stiffness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Rotational Restraint to client model
        Model.clientModel.service.set_member_rotational_restraint(clientObject)
