"""
    Partner Experience Cloud API Python SDK

    Partner Experience Cloud API Python SDK - LA Release  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pxcloud_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from pxcloud_api_client.exceptions import ApiAttributeError


def lazy_import():
    from pxcloud_api_client.model.suggestion_summary_advisories_severity import SuggestionSummaryAdvisoriesSeverity
    from pxcloud_api_client.model.suggestion_summary_bug_severity import SuggestionSummaryBugSeverity
    from pxcloud_api_client.model.suggestion_summary_features_count import SuggestionSummaryFeaturesCount
    from pxcloud_api_client.model.suggestion_summary_field_notice_severity import SuggestionSummaryFieldNoticeSeverity
    globals()['SuggestionSummaryAdvisoriesSeverity'] = SuggestionSummaryAdvisoriesSeverity
    globals()['SuggestionSummaryBugSeverity'] = SuggestionSummaryBugSeverity
    globals()['SuggestionSummaryFeaturesCount'] = SuggestionSummaryFeaturesCount
    globals()['SuggestionSummaryFieldNoticeSeverity'] = SuggestionSummaryFieldNoticeSeverity


class SuggestionSummary(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'expected_software_group_risk': (str,),  # noqa: E501
            'expected_software_group_risk_category': (str,),  # noqa: E501
            'machine_suggestion_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'release_date': (datetime,),  # noqa: E501
            'release': (str,),  # noqa: E501
            'release_notes_url': (str,),  # noqa: E501
            'bug_severity': (SuggestionSummaryBugSeverity,),  # noqa: E501
            'advisories_severity': (SuggestionSummaryAdvisoriesSeverity,),  # noqa: E501
            'field_notice_severity': (SuggestionSummaryFieldNoticeSeverity,),  # noqa: E501
            'features_count': (SuggestionSummaryFeaturesCount,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'expected_software_group_risk': 'expectedSoftwareGroupRisk',  # noqa: E501
        'expected_software_group_risk_category': 'expectedSoftwareGroupRiskCategory',  # noqa: E501
        'machine_suggestion_id': 'machineSuggestionId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'release_date': 'releaseDate',  # noqa: E501
        'release': 'release',  # noqa: E501
        'release_notes_url': 'releaseNotesUrl',  # noqa: E501
        'bug_severity': 'bugSeverity',  # noqa: E501
        'advisories_severity': 'advisoriesSeverity',  # noqa: E501
        'field_notice_severity': 'fieldNoticeSeverity',  # noqa: E501
        'features_count': 'featuresCount',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SuggestionSummary - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            expected_software_group_risk (str): Current risk score of the Cisco software release, which is the level of exposure the software release has to bugs, security advisories, and field notices. The risk score is used to make software suggestions intended to minimize risk for assets in the Software Group.. [optional]  # noqa: E501
            expected_software_group_risk_category (str): Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low.. [optional]  # noqa: E501
            machine_suggestion_id (str): Unique identifier of the suggestion. [optional]  # noqa: E501
            name (str): Value that indicates whether the Cisco software release is a current release or one of the suggested release options. [optional]  # noqa: E501
            release_date (datetime): Date the Cisco software image was released. [optional]  # noqa: E501
            release (str): Release of the Cisco software. [optional]  # noqa: E501
            release_notes_url (str): Public URL for the release notes of the Cisco software release. [optional]  # noqa: E501
            bug_severity (SuggestionSummaryBugSeverity): [optional]  # noqa: E501
            advisories_severity (SuggestionSummaryAdvisoriesSeverity): [optional]  # noqa: E501
            field_notice_severity (SuggestionSummaryFieldNoticeSeverity): [optional]  # noqa: E501
            features_count (SuggestionSummaryFeaturesCount): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SuggestionSummary - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            expected_software_group_risk (str): Current risk score of the Cisco software release, which is the level of exposure the software release has to bugs, security advisories, and field notices. The risk score is used to make software suggestions intended to minimize risk for assets in the Software Group.. [optional]  # noqa: E501
            expected_software_group_risk_category (str): Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low.. [optional]  # noqa: E501
            machine_suggestion_id (str): Unique identifier of the suggestion. [optional]  # noqa: E501
            name (str): Value that indicates whether the Cisco software release is a current release or one of the suggested release options. [optional]  # noqa: E501
            release_date (datetime): Date the Cisco software image was released. [optional]  # noqa: E501
            release (str): Release of the Cisco software. [optional]  # noqa: E501
            release_notes_url (str): Public URL for the release notes of the Cisco software release. [optional]  # noqa: E501
            bug_severity (SuggestionSummaryBugSeverity): [optional]  # noqa: E501
            advisories_severity (SuggestionSummaryAdvisoriesSeverity): [optional]  # noqa: E501
            field_notice_severity (SuggestionSummaryFieldNoticeSeverity): [optional]  # noqa: E501
            features_count (SuggestionSummaryFeaturesCount): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
