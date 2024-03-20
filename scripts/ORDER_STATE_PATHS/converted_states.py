QUEUED = "queued"
SUBMITTING = "submitting"
SUBMITTED = "submitted"
PROCESSING = "processing"
BUMPED = "bumped"
ASSIGNED = "assigned"
COMPLETION_PENDING = "completion_pending"
COMPLETED = "completed"
REFUNDED = "refunded"
PARTIALLY_REFUNDED = "partially_refunded"
INCOMPLETE = "incomplete"
DELIVERY_FAILED = "delivery_failed"
SUBMISSION_FAILED = "submission_failed"
CLOSED_BY_ADMIN = "closed_by_admin"
AUTHORIZATION_FAILED = "authorization_failed"
SETTLEMENT_FAILED = "settlement_failed"
CANCELLED = "cancelled"
DELIVERED_WITHOUT_ALCOHOL = "delivered_without_alcohol"
PROBLEM_REPORTED = "problem_reported"
REFUND_FAILED = "refund_failed"
NOT_COLLECTED = "not_collected"
APPROVED_OFFLINE = "approved_offline"
TABBED = "tabbed"

STATES = set(["queued", "submitting", "submitted", "processing", "bumped", "assigned", "completion_pending", "completed", "refunded", "partially_refunded", "incomplete", "delivery_failed", "submission_failed", "closed_by_admin", "authorization_failed", "settlement_failed", "cancelled", "delivered_without_alcohol", "problem_reported", "refund_failed", "not_collected", "approved_offline", "tabbed"])

NON_REFUNDABLE_STATES = set([ SETTLEMENT_FAILED, COMPLETION_PENDING ])
VALID_RESUBMIT_STATES   = set([AUTHORIZATION_FAILED, SUBMISSION_FAILED])
SUCCESSFUL_FINAL_STATES = set([COMPLETED, DELIVERED_WITHOUT_ALCOHOL, NOT_COLLECTED])
STOP_TRACKING_USER_STATES = set([COMPLETED, DELIVERED_WITHOUT_ALCOHOL, COMPLETION_PENDING, CANCELLED, PROBLEM_REPORTED, SUBMISSION_FAILED, NOT_COLLECTED])
FRIEND_TEXT_ORDER_RECEIVED_STATES = set([QUEUED, SUBMITTING, SUBMITTED])
FRIEND_TEXT_ORDER_COMING_STATES = set([BUMPED, ASSIGNED])
FINAL_RUNNER_STATES = set([COMPLETED, DELIVERED_WITHOUT_ALCOHOL, COMPLETION_PENDING, PROBLEM_REPORTED, DELIVERY_FAILED, NOT_COLLECTED])
ALL_BUT_INCOMPLETE_STATES = STATES - set([INCOMPLETE])
PROBLEM_REPORTED_STATES = set([PROBLEM_REPORTED])


VALID_STATES_PATH = {
    "queued": STATES.difference((("authorization_failed", "queued", "incomplete") + tuple(FINAL_RUNNER_STATES))),
    "submitting": STATES.difference("authorization_failed", "queued", "incomplete", "submitting", "cancelled"),
    "submitted": STATES.difference("queued", "incomplete", "submitting", "submitted"),
    "processing": STATES.difference("authorization_failed", "queued", "incomplete", "submitting", "submitted", "submission_failed"),
    "bumped": STATES.difference("authorization_failed", "queued", "incomplete", "submitting", "submitted", "submission_failed", "processing"),
    "assigned": STATES.difference("authorization_failed", "queued", "incomplete", "submitting", "submitted", "submission_failed", "processing"),
    "completion_pending": ("completion_pending", "completed", "cancelled", "delivery_failed", "closed_by_admin", "settlement_failed"),
    "completed": ("settlement_failed", "delivered_without_alcohol", "problem_reported"),
    "refunded": (),
    "partially_refunded": ("refunded", "refund_failed"),
    "incomplete": (ALL_BUT_INCOMPLETE_STATES - FINAL_RUNNER_STATES),
    "delivery_failed": PROBLEM_REPORTED_STATES,
    "submission_failed": ALL_BUT_INCOMPLETE_STATES,
    "closed_by_admin": (),
    "authorization_failed": ALL_BUT_INCOMPLETE_STATES,
    "settlement_failed": ("completed", "tabbed"),
    "cancelled": (),
    "delivered_without_alcohol": ("refunded", "partially_refunded", "refund_failed", "problem_reported"),
    "problem_reported": (),
    "refund_failed": ("refunded", "partially_refunded"),
    "not_collected": ("refunded", "partially_refunded", "refund_failed", "problem_reported"),
    "approved_offline": STATES,
}


# def print_valid_states():
#     for state, valid_states in VALID_STATES_PATH.items():
#         print(f"State: {state}")
#         print("Valid next states:")
#         for valid_state in valid_states:
#             print(f" - {valid_state}")
#         print()
        
# def write_valid_states_to_file(filename):
#     with open(filename, 'w') as file:
#         for state, valid_states in VALID_STATES_PATH.items():
#             file.write(f"State: {state}\n")
#             file.write("Valid next states:\n")
#             for valid_state in valid_states:
#                 file.write(f" - {valid_state}\n")
#             file.write("\n")

def write_valid_states_to_file(filename):
    with open(filename, 'w') as file:
        file.write("All States and Valid Next States:\n")
        file.write("---------------------------------\n")
        for state, valid_states in VALID_STATES_PATH.items():
            file.write(f"State: {state}\n")
            file.write("Valid next states:\n")
            for valid_state in valid_states:
                file.write(f" - {valid_state}\n")
            file.write("\n")

        #completable states
        file.write("\nCompletable States (States that can lead to 'completed'):\n")
        file.write("---------------------------------------------------------\n")
        for state, valid_states in VALID_STATES_PATH.items():
            if 'completed' in valid_states:
                file.write(f"{state}\n")
                
        # all order states
        file.write("\nAll Order States:\n")
        file.write("---------------------------------------------------------\n")
        for state in STATES:
            file.write(f"{state}\n")


if __name__ == "__main__":
    output_filename = "scripts/ORDER_STATE_PATHS/valid_states_output.txt"
    write_valid_states_to_file(output_filename)

