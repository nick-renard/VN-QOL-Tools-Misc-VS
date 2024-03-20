module Order::States

  # WARNING: ALL order states should be downcased.
  STATES = [
    # happy path states:
    QUEUED = "queued", # order has been placed with Stadium but not yet submitted to pos
    SUBMITTING = "submitting", # Stadium has marked it as ready to submit and queued a job to submit it
    SUBMITTED = "submitted", # submitted to pos, we don't have any status update back from them yet
    PROCESSING = "processing", # received by pos, is on the KDS
        # in-seat: delivery we go to KDS
        # express: no statuses, eoss will not know about it until paid
    BUMPED = "bumped", # expediter taps screen to remove it from KDS and send it to printer
        # order is being prepared
    ASSIGNED = "assigned", # the runner has it
    COMPLETION_PENDING = "completion_pending", #delivered, but not completed in POS
        # order is on the way
    COMPLETED = "completed",
    REFUNDED = "refunded", # full refund after order settlement
    PARTIALLY_REFUNDED = "partially_refunded", # partial refund after order settlement

    # unhappy path states:
    INCOMPLETE = "incomplete",
    DELIVERY_FAILED = "delivery_failed", # runner cannot find end user
    SUBMISSION_FAILED = "submission_failed", # a problem with pos or the network prevents us from submitting
    CLOSED_BY_ADMIN = "closed_by_admin",
    AUTHORIZATION_FAILED = "authorization_failed", # payment authorization failed
    SETTLEMENT_FAILED = "settlement_failed", # payment settlement failed
    CANCELLED = "cancelled",
    DELIVERED_WITHOUT_ALCOHOL = "delivered_without_alcohol", # delivered, but alcohol removed from the order
    PROBLEM_REPORTED = "problem_reported", # end user didn't receive their order, or items were damaged or missing
    REFUND_FAILED = "refund_failed", # admins can refund orders after they've been settled
    NOT_COLLECTED = "not_collected", # order never picked up by user. charged as normal; does not trigger a refund

    # virtual states (immobile)
    APPROVED_OFFLINE = "approved_offline", # this order was approved offline but not completed
    TABBED = "tabbed" # the order is in a tab state
  ]

  NON_REFUNDABLE_STATES = [ SETTLEMENT_FAILED, COMPLETION_PENDING ]
  REFUNDABLE_STATES = STATES - NON_REFUNDABLE_STATES
  VALID_RESUBMIT_STATES   = [AUTHORIZATION_FAILED, SUBMISSION_FAILED]
  SUCCESSFUL_FINAL_STATES = [COMPLETED, DELIVERED_WITHOUT_ALCOHOL, NOT_COLLECTED]
  STOP_TRACKING_USER_STATES = [COMPLETED, DELIVERED_WITHOUT_ALCOHOL, COMPLETION_PENDING, CANCELLED, PROBLEM_REPORTED, SUBMISSION_FAILED, NOT_COLLECTED]
  FRIEND_TEXT_ORDER_RECEIVED_STATES = [QUEUED, SUBMITTING, SUBMITTED]
  FRIEND_TEXT_ORDER_COMING_STATES = [BUMPED, ASSIGNED]
  FINAL_RUNNER_STATES = [COMPLETED, DELIVERED_WITHOUT_ALCOHOL, COMPLETION_PENDING, PROBLEM_REPORTED, DELIVERY_FAILED, NOT_COLLECTED]
  ALL_BUT_INCOMPLETE_STATES = STATES - [INCOMPLETE]

  VALID_STATES_PATH = {
    QUEUED => STATES - ([AUTHORIZATION_FAILED, QUEUED, INCOMPLETE] + FINAL_RUNNER_STATES),
    SUBMITTING => STATES - [AUTHORIZATION_FAILED, QUEUED, INCOMPLETE, SUBMITTING, CANCELLED],
    SUBMITTED => STATES - [QUEUED, INCOMPLETE, SUBMITTING, SUBMITTED],
    PROCESSING => STATES - [AUTHORIZATION_FAILED, QUEUED, INCOMPLETE, SUBMITTING, SUBMITTED, SUBMISSION_FAILED,
      PROCESSING],
    BUMPED => STATES - [AUTHORIZATION_FAILED, QUEUED, INCOMPLETE, SUBMITTING, SUBMITTED, SUBMISSION_FAILED, PROCESSING,
      BUMPED],
    ASSIGNED => STATES - [AUTHORIZATION_FAILED, QUEUED, INCOMPLETE, SUBMITTING, SUBMITTED, SUBMISSION_FAILED, PROCESSING,
      ASSIGNED],
    COMPLETION_PENDING => [COMPLETION_PENDING, COMPLETED, CANCELLED, DELIVERY_FAILED, CLOSED_BY_ADMIN, SETTLEMENT_FAILED,
      DELIVERED_WITHOUT_ALCOHOL, PROBLEM_REPORTED],
    COMPLETED => [SETTLEMENT_FAILED, DELIVERED_WITHOUT_ALCOHOL, PROBLEM_REPORTED],
    REFUNDED => [],
    PARTIALLY_REFUNDED => [REFUNDED, REFUND_FAILED],
    INCOMPLETE => ALL_BUT_INCOMPLETE_STATES - FINAL_RUNNER_STATES,
    DELIVERY_FAILED => [PROBLEM_REPORTED],
    SUBMISSION_FAILED => ALL_BUT_INCOMPLETE_STATES,
    CLOSED_BY_ADMIN => [],
    AUTHORIZATION_FAILED => ALL_BUT_INCOMPLETE_STATES,
    SETTLEMENT_FAILED => [COMPLETED, TABBED],
    CANCELLED => [],
    DELIVERED_WITHOUT_ALCOHOL => [REFUNDED, PARTIALLY_REFUNDED, REFUND_FAILED, PROBLEM_REPORTED],
    PROBLEM_REPORTED => [],
    REFUND_FAILED => [REFUNDED, PARTIALLY_REFUNDED],
    NOT_COLLECTED => [REFUNDED, PARTIALLY_REFUNDED, REFUND_FAILED, PROBLEM_REPORTED],
    APPROVED_OFFLINE => STATES,
    TABBED => STATES
  }

  OPEN_STATES = [INCOMPLETE, SUBMITTING, QUEUED, SUBMITTED, PROCESSING, BUMPED, APPROVED_OFFLINE, TABBED]
  PENDING_STATES = [QUEUED, SUBMITTED, SUBMITTING, PROCESSING, BUMPED, ASSIGNED]
  RECONCILABLE_STATES = OPEN_STATES + [COMPLETION_PENDING, ASSIGNED]

  PRODUCTION_LINE_STATE = PROCESSING

  XPEDITE_STATES = {
    "PROCESSING" => "processing",
    "BUMPED" => "bumped",
    "ASSIGNED" => "assigned",
    "DELIVERY_FAILED" => "DeliveryFailed",
    "COMPLETED" => "completed",
    "BUMP" => "bump",
    "ASSIGN" => "assign",
    "COMPLETE" => "complete",
    "CLOSED" => "Closed",
    "DELIVERED_WITHOUT_ALCOHOL" => "DeliveredNoAlcohol"
  }

  VALID_CANCEL_STATES = {
    ServiceTypes::DELIVERY           => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::FRIEND_DELIVERY    => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::TABLE              => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::PICKUP             => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::CARRY_OUT          => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::DELIVER_FOR_PICKUP => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::DELIVERY_FIND      => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::ROOM_DELIVERY      => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::CONCESSIONS        => [QUEUED, INCOMPLETE, SUBMITTED, AUTHORIZATION_FAILED],
    ServiceTypes::ORDER_AHEAD        => [QUEUED, INCOMPLETE, SUBMITTED, AUTHORIZATION_FAILED],
    ServiceTypes::QUICK_PAY          => [QUEUED, INCOMPLETE, SUBMITTED, AUTHORIZATION_FAILED],
    ServiceTypes::KIOSK              => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::POS                => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED, APPROVED_OFFLINE, TABBED],
    ServiceTypes::USER               => [QUEUED, INCOMPLETE, SUBMITTED, AUTHORIZATION_FAILED],
    ServiceTypes::PRE_ORDER          => [QUEUED, INCOMPLETE, DELIVERY_FAILED, SUBMISSION_FAILED, AUTHORIZATION_FAILED],
    ServiceTypes::SELF_CHECKOUT      => [QUEUED, INCOMPLETE, SUBMITTED, AUTHORIZATION_FAILED]
  }

  VALID_CANCEL_BY_USER_STATES = {
    ServiceTypes::DELIVERY           => [QUEUED],
    ServiceTypes::FRIEND_DELIVERY    => [QUEUED],
    ServiceTypes::TABLE              => [QUEUED],
    ServiceTypes::PICKUP             => [QUEUED],
    ServiceTypes::CARRY_OUT          => [QUEUED],
    ServiceTypes::DELIVER_FOR_PICKUP => [QUEUED],
    ServiceTypes::DELIVERY_FIND      => [QUEUED],
    ServiceTypes::ROOM_DELIVERY      => [QUEUED],
    ServiceTypes::CONCESSIONS        => [QUEUED, SUBMITTED],
    ServiceTypes::ORDER_AHEAD        => [QUEUED, SUBMITTED],
    ServiceTypes::QUICK_PAY          => [QUEUED, SUBMITTED],
    ServiceTypes::KIOSK              => [QUEUED],
    ServiceTypes::POS                => [QUEUED, APPROVED_OFFLINE, TABBED],
    ServiceTypes::USER               => [QUEUED, SUBMITTED],
    ServiceTypes::PRE_ORDER          => [QUEUED],
    ServiceTypes::SELF_CHECKOUT      => [QUEUED, SUBMITTED]
  }

  VALID_MODIFY_BY_USER_STATES = {
    # currently only queued kds orders are modifiable
    ServiceTypes::DELIVERY           => [QUEUED],
    ServiceTypes::FRIEND_DELIVERY    => [QUEUED],
    ServiceTypes::TABLE              => [QUEUED],
    ServiceTypes::PICKUP             => [QUEUED],
    ServiceTypes::CARRY_OUT          => [QUEUED],
    ServiceTypes::DELIVER_FOR_PICKUP => [QUEUED],
    ServiceTypes::DELIVERY_FIND      => [QUEUED],
    ServiceTypes::ROOM_DELIVERY      => [QUEUED],
    ServiceTypes::CONCESSIONS        => [],
    ServiceTypes::ORDER_AHEAD        => [],
    ServiceTypes::QUICK_PAY          => [],
    ServiceTypes::KIOSK              => [QUEUED],
    ServiceTypes::POS                => [QUEUED, APPROVED_OFFLINE, TABBED],
    ServiceTypes::USER               => [],
    ServiceTypes::PRE_ORDER          => [QUEUED],
    ServiceTypes::SELF_CHECKOUT      => []
  }

  REMOVE_ALCOHOL_STATES = [DELIVERED_WITHOUT_ALCOHOL]

  SHOW_REPORT_PROBLEM_IMMEDIATELY_STATES = [DELIVERY_FAILED, DELIVERED_WITHOUT_ALCOHOL, COMPLETION_PENDING, COMPLETED, NOT_COLLECTED]
  SHOW_REPORT_PROBLEM_AFTER_TIME_STATES  = [BUMPED, ASSIGNED, SUBMITTED]
  EXCLUDED_REPORT_ORDERS_STATES = [AUTHORIZATION_FAILED, SUBMITTED, SUBMISSION_FAILED]

  DEFAULT_POS_ORDERS_INDEX_STATES = [COMPLETED, COMPLETION_PENDING, INCOMPLETE, TABBED]

  NON_POLLABLE = [
    Order::States::PROBLEM_REPORTED, Order::States::DELIVERED_WITHOUT_ALCOHOL,
    Order::States::REFUND_FAILED, Order::States::SETTLEMENT_FAILED, Order::States::CANCELLED,
    Order::States::INCOMPLETE, Order::States::DELIVERY_FAILED, Order::States::QUEUED,
    Order::States::SUBMITTING, Order::States::SUBMISSION_FAILED, Order::States::CLOSED_BY_ADMIN,
    Order::States::COMPLETED, Order::States::NOT_COLLECTED
  ]
end
