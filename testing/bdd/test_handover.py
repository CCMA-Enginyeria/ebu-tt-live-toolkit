
import pytest
from pytest_bdd import scenarios, given, when, then
from ebu_tt_live.node import handover as handover_node
from ebu_tt_live.documents import EBUTT3Document
from ebu_tt_live.carriage.interface import IProducerCarriage
from mock import MagicMock


scenarios('features/handover/handover_algorithm.feature')


@given('a handover node with <authors_group_identifier> and <sequence_identifier>')
def given_handover_node(authors_group_identifier, sequence_identifier):
    carriage = MagicMock(spec=IProducerCarriage)
    carriage.expects.return_value = EBUTT3Document
    instance = handover_node.HandoverNode(
        node_id='testHandoverNode',
        authors_group_identifier=authors_group_identifier,
        sequence_identifier=sequence_identifier,
        producer_carriage=carriage
    )
    return instance


@when('it has <sequence_identifier1> and <sequence_number1>')
def when_sequence_id_and_num_1(sequence_identifier1, sequence_number1, template_dict):
    template_dict['sequence_identifier'] = sequence_identifier1
    template_dict['sequence_number'] = sequence_number1


@when('it has <sequence_identifier2> and <sequence_number2>')
def when_sequence_id_and_num_2(sequence_identifier2, sequence_number2, template_dict):
    template_dict['sequence_identifier'] = sequence_identifier2
    template_dict['sequence_number'] = sequence_number2


@when('it has <authors_group_identifier>')
def when_authors_group_id(template_dict, authors_group_identifier):
    template_dict['authors_group_identifier'] = authors_group_identifier
    
    
@when('it has <authors_group_control_token1>')
def when_authors_group_token1(template_dict, authors_group_control_token1):
    template_dict['authors_group_control_token'] = authors_group_control_token1
    

@when('it has <authors_group_control_token2>')
def when_authors_group_token2(template_dict, authors_group_control_token2):
    template_dict['authors_group_control_token'] = authors_group_control_token2


@when('new document is created')
def new_doc_created(template_dict):
    template_dict.clear()


@when('handover node processes document')
def new_document(test_context, given_handover_node):
    given_handover_node.process_document(test_context['document'])


@then('handover node emits <emitted_documents> documents')
def then_handover_node_emits(given_handover_node, emitted_documents):
    assert given_handover_node.producer_carriage.emit_data.call_count == int(emitted_documents)
