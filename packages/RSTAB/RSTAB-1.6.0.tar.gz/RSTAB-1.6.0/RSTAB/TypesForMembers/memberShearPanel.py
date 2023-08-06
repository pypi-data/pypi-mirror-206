from RSTAB.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RSTAB.enums import MemberShearPanelDefinitionType, MemberShearPanelFasteningArrangement, MemberShearPanelPositionOnSection

class MemberShearPanel():

    def __init__(self) -> None:
        pass

    @staticmethod
    def TrapezodialSheeting(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        position_on_section = MemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE,
        girder_length_definition: list = [True],
        sheeting_name: str = 'FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil',
        fastening_arrangement = MemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB,
        panel_length: float = 2.0,
        beam_spacing: float = 1.0,
        coefficient_k1: float = 0.0002,
        coefficient_k2: float = 0.0123,
        position_on_section_value: float = 1.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            position_on_section (enum): Member Shear Panel Position Enumeration
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (boolean): Definition Option
                girder_length_definition[1] (enum): Definition Type Enumeration
            sheeting_name (str): Sheeting Name
            fastening_arrangement (enum): Fastening Arrangement Enumeration
            panel_length (float): Panel Length
            beam_spacing (float): Beam Spacing
            coefficient_k1 (float): Coefficient K1
            coefficient_k2 (float): Coefficient K2
            position_on_section_value (float): Position on Section Value
            comment (str, optional): Comment
            params (dict, optional): Parameters
        """

        # Client Model | Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING.name

        # Member Shear Panel Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Position On Section
        clientObject.position_on_section = position_on_section.name

        if position_on_section == MemberShearPanelPositionOnSection.POSITION_DEFINE:
            clientObject.position_on_section_value = position_on_section_value

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Sheeting Name
        clientObject.sheeting_name = sheeting_name

        # Member Shear Panel Fastening Arrangement
        clientObject.fastening_arrangement = fastening_arrangement.name

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Coefficient K1
        clientObject.coefficient_k1 = coefficient_k1

        # Member Shear Panel Coefficient K2
        clientObject.coefficient_k2 = coefficient_k2

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        Model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def Bracing(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        position_on_section = MemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE,
        girder_length_definition: list = [True],
        material_name: str = 'S235',
        diagonal_section: str = 'CHC 60.3x4.0',
        posts_section: str = 'CHC 76.1x4.0',
        modulus_of_elasticity: float = 210000000000.0,
        panel_length: float = 2.0,
        beam_spacing: float = 1.0,
        posts_spacing: float = 2.0,
        number_of_bracings: int = 2,
        diagonals_section_area: float = 0.001007,
        posts_section_area: float = 0.0009,
        position_on_section_value: float = 1.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            position_on_section (enum): Member Shear Panel Position Enumeration
            material_name (str): Material Name
            diagonal_section (str): Diagonal Section
            posts_section (str): Posts Section
            modulus_of_elasticity (float): Modulus of Elasticity
            panel_length (float): Panel Length
            beam_spacing (float): Beam Spacing
            posts_spacing (float): Posts Spacing
            number_of_bracings (int): Number of Bracings
            diagonals_section_area (float): Diagonals Section Area
            posts_section_area (float): Posts Section Area
            position_on_section_value (float): Position of Section Value
            comment (str, optional): Comment
            params (dict, optional): Params
        """

        # Client Model | Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_BRACING.name

        # Member Shear Panel Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Position On Section
        clientObject.position_on_section = position_on_section.name

        if position_on_section == MemberShearPanelPositionOnSection.POSITION_DEFINE:
            clientObject.position_on_section_value = position_on_section_value

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Material Name
        clientObject.material_name = material_name

        # Member Shear Panel Diagonal Section
        clientObject.diagonals_section_name = diagonal_section

        # Member Shear Panel Posts Section
        clientObject.posts_section_name = posts_section

        # Member Shear Panel Modulus of Elasticity
        clientObject.modulus_of_elasticity = modulus_of_elasticity

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Posts Spacing
        clientObject.post_spacing = posts_spacing

        # Member Shear Panel Number of Bracing
        clientObject.number_of_bracings = number_of_bracings

        # Member Shear Panel Diagonals Section Area
        clientObject.diagonals_section_area = diagonals_section_area

        # Member Shear Panel Posts Section Area
        clientObject.posts_section_area = posts_section_area

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        Model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def DefineSProv(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        position_on_section = MemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE,
        girder_length_definition: list = [True],
        shear_panel_stiffness: float = 1000.0,
        position_on_section_value: float = 1.0,
        comment: str = '',
        params: dict = None):
        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            position_on_section (enum): Position on Section Enumeration
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (boolean): Definition Option
                girder_length_definition[1] (enum): Definition Type Enumeration
            shear_panel_stiffness (float): Shear Panel Stiffness
            position_on_section_value (float): Position on Section Value
            comment (str, optional): Comment
            params (dict, optional): Parameters
        """
        # Client Model | Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_DEFINE_S_PROV.name

        # Member Shear Panel Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Position On Section
        clientObject.position_on_section = position_on_section.name

        if position_on_section == MemberShearPanelPositionOnSection.POSITION_DEFINE:
            clientObject.position_on_section_value = position_on_section_value

        # Member Shear Panel Stiffness
        clientObject.stiffness = shear_panel_stiffness

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        Model.clientModel.service.set_member_shear_panel(clientObject)

    @staticmethod
    def TrapeziodalSheetingAndBracing(
        no: int = 1,
        name: str = '',
        member_supports: str = '1',
        position_on_section = MemberShearPanelPositionOnSection.POSITION_ON_UPPER_FLANGE,
        sheeting_name: str = 'FI (+) 35/207 - 0.63 (b: 1) | DIN 18807 | Fischer Profil',
        material_name: str = 'S235',
        diagonals_section: str = 'CHC 60.3x3.2',
        posts_section: str = 'CHC 76.1x4.0',
        fastening_arrangement = MemberShearPanelFasteningArrangement.FASTENING_ARRANGEMENT_EVERY_RIB,
        modulus_of_elasticity: float = 205000000000.0,
        panel_length: float = 1.0,
        girder_length_definition: list = [True],
        beam_spacing: float = 2.0,
        coefficient_k1: float = 0.0002,
        coefficient_k2: float = 0.0104,
        post_spacing: float = 3.0,
        number_of_bracing: int = 2,
        diagonals_section_area: float = 0.0005,
        posts_section_area = 0.0009,
        position_on_section_value = 1.0,
        comment: str = '',
        params: dict = None
    ):
        """
        Args:
            no (int): Member Shear Panel Tag
            name (str): Member Shear Panel Name
                if name == '':
                    name = False (Automatic Name Assignment)
                else:
                    name = name
            member_supports (str): Assigned Member Supports
            position_on_section (enum): Position on Section Enumeration
            sheeting_name (str): Sheeting Name
            material_name (str): Material Name
            diagonals_section (str): Diagonals Section
            posts_section (str): Posts Section
            fastening_arrangement (enum): Fastening Arrangement Enumeration
            modulus_of_elasticity (float): Modulus of Elasticity
            panel_length (float): Panel Length
            girder_length_definition (list): Girder Length Definition List
                girder_length_definition[0] (boolean): Definition Option
                girder_length_definition[1] (enum): Definition Type Enumeration
            beam_spacing (float): Beam Spacing
            coefficient_k1 (float): Coefficient K1
            coefficient_k2 (float): Coefficient K2
            post_spacing (float): Posts Spacing
            number_of_bracing (int): Number of Bracings
            diagonals_section_area (float): Diagonals Section Area
            posts_section_area (float): Posts Section Area
            position_on_section_value (float): Position on Section Value
            comment (str, optional): Comment
            params (dict, optional): Parameters
        """
        # Client Model | Member Shear Panel
        clientObject = Model.clientModel.factory.create('ns0:member_shear_panel')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Shear Panel No.
        clientObject.no = no

        # Member Shear Panel Definition Type
        clientObject.definition_type = MemberShearPanelDefinitionType.DEFINITION_TYPE_TRAPEZOIDAL_SHEETING_AND_BRACING.name

        # Member Shear Panel Assigned Member Supports
        clientObject.member_supports = ConvertToDlString(member_supports)

        # Member Shear Panel User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Member Shear Panel Position On Section
        clientObject.position_on_section = position_on_section.name

        if position_on_section == MemberShearPanelPositionOnSection.POSITION_DEFINE:
            clientObject.position_on_section_value = position_on_section_value

        # Member Shear Panel Sheeting Name
        clientObject.sheeting_name = sheeting_name

        # Member Shear Panel Material Name
        clientObject.material_name = material_name

        # Member Shear Panel Diagonals Section
        clientObject.diagonals_section_name = diagonals_section

        # Member Shear Panel Posts Section
        clientObject.posts_section_name = posts_section

        # Member Shear Panel Fastening Arrangement
        clientObject.fastening_arrangement = fastening_arrangement.name

        # Member Shear Panel Modulus of Elasticity
        clientObject.modulus_of_elasticity= modulus_of_elasticity

        # Member Shear Panel Panel Length
        clientObject.panel_length = panel_length

        # Member Shear Panel Beam Spacing
        clientObject.beam_spacing = beam_spacing

        # Member Shear Panel Girder Length Definition
        if girder_length_definition[0]:
            clientObject.define_girder_length_automatically = True
        else:
            clientObject.define_girder_length_automatically = False
            clientObject.girder_length = girder_length_definition[1]

        # Member Shear Panel Coefficients
        clientObject.coefficient_k1 = coefficient_k1
        clientObject.coefficient_k2 = coefficient_k2

        # Member Shear Panel Posts Spacings
        clientObject.post_spacing = post_spacing

        # Member Shear Panel Number of Bracing
        clientObject.number_of_bracings = number_of_bracing

        # Member Shear Panel Diagonals Section Area
        clientObject.diagonals_section_area = diagonals_section_area

        # Member Shear Panel Posts Section Area
        clientObject.posts_section_area = posts_section_area

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Shear Panel to client model
        Model.clientModel.service.set_member_shear_panel(clientObject)
