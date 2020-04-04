with section("parse"):
  additional_commands = { 'foo': { 'flags': ['BAR', 'BAZ'],
             'kwargs': {'DEPENDS': '*', 'HEADERS': '*', 'SOURCES': '*'}}}
  vartags = []
  proptags = []

with section("format"):
  line_width = 80
  tab_size = 2
  max_subgroups_hwrap = 2
  max_pargs_hwrap = 6
  max_rows_cmdline = 2
  separate_ctrl_name_with_space = False
  separate_fn_name_with_space = False
  dangle_parens = False
  dangle_align = 'prefix'
  min_prefix_chars = 4
  max_prefix_chars = 10
  max_lines_hwrap = 2
  line_ending = 'unix'
  command_case = 'canonical'
  keyword_case = 'unchanged'
  always_wrap = []
  enable_sort = True
  autosort = False
  require_valid_layout = False
  layout_passes = {}

with section("markup"):
  bullet_char = '*'
  enum_char = '.'
  first_comment_is_literal = False
  literal_comment_pattern = None
  fence_pattern = '^\\s*([`~]{3}[`~]*)(.*)$'
  ruler_pattern = '^\\s*[^\\w\\s]{3}.*[^\\w\\s]{3}$'
  explicit_trailing_pattern = '#<'
  hashruler_min_length = 10
  canonicalize_hashrulers = True
  enable_markup = True

with section("lint"):
  disabled_codes = []
  function_pattern = '[0-9a-z_]+'
  macro_pattern = '[0-9A-Z_]+'
  global_var_pattern = '[0-9A-Z][0-9A-Z_]+'
  internal_var_pattern = '_[0-9A-Z][0-9A-Z_]+'
  local_var_pattern = '[0-9a-z_]+'
  private_var_pattern = '_[0-9a-z_]+'
  public_var_pattern = '[0-9A-Z][0-9A-Z_]+'
  keyword_pattern = '[0-9A-Z_]+'
  max_conditionals_custom_parser = 2
  min_statement_spacing = 1
  max_statement_spacing = 1
  max_returns = 6
  max_branches = 12
  max_arguments = 5
  max_localvars = 15
  max_statements = 50

with section("encode"):
  emit_byteorder_mark = False
  input_encoding = 'utf-8'
  output_encoding = 'utf-8'

with section("misc"):
  per_command = {}

