const { SCHEME, HOSTNAME } =
  process.env.NODE_ENV === 'production'
    ? {SCHEME: 'https', HOSTNAME: window.location.host}
    : {SCHEME: 'http', HOSTNAME: '127.0.0.1:8001'}

const API_URL = `${SCHEME}://${HOSTNAME}/api/v1`
const SESSION_URL = `${API_URL}/auth/`
const CURRENT_USER_URL = `${API_URL}/user_info/`
const AUDIT_PERSON_URL = `${API_URL}/audit_person/`
const AUDIT_RES_GROUP_URL = `${API_URL}/audit_res_group/`
const AUDIT_PERSON_GROUP_URL = `${API_URL}/audit_person_group/`
const AUDIT_RES_URL = `${API_URL}/audit_res/`
const AUDIT_PERMISSION_URL = `${API_URL}/permission_res/`
const AUDIT_RES_ACCOUNT_URL = `${API_URL}/audit_res_account/`
const AUDIT_RES_ACCOUNT_REL_URL = `${API_URL}/audit_res_account_rel/`
const USER_TASK = `${API_URL}/user_task/`
const USER_TASK_LIST = `${API_URL}/user_task_list/`
const USER_TASK_DETAIL = `${API_URL}/user_task_detail/`
const TASK_USER_INFO = `${API_URL}/task_user_info/`
const USER_TASK_COUNT = `${API_URL}/user_task_count/`
const USER_TASK_DELETE = `${API_URL}/user_task_delete/`
const USER_TASK_APPLYTYPE = `${API_URL}/applytype/`
const USER_DETAIL = `${API_URL}/user_detail/`

export default {
  SESSION_URL,
  CURRENT_USER_URL,
  AUDIT_PERSON_URL,
  AUDIT_RES_GROUP_URL,
  AUDIT_PERSON_GROUP_URL,
  AUDIT_RES_URL,
  AUDIT_PERMISSION_URL,
  AUDIT_RES_ACCOUNT_URL,
  AUDIT_RES_ACCOUNT_REL_URL,
  USER_TASK,
  USER_TASK_LIST,
  USER_TASK_DETAIL,
  TASK_USER_INFO,
  USER_TASK_COUNT,
  USER_TASK_DELETE,
  USER_TASK_APPLYTYPE,
  USER_DETAIL
}

