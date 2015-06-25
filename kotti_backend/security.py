# No allow view for everyone.
# This is the ACL that gets set on the site root on creation.  Note
# that this is only really useful if you're _not_ using workflow.  If
# you are, then you should look at the permissions in workflow.zcml.
SITE_ACL = [
    # ['Allow', 'system.Everyone', ['view']],
    ['Allow', 'system.Everyone', ['pview']],
    ['Allow', 'role:viewer', ['view']],
    ['Allow', 'role:editor', ['view', 'add', 'edit', 'state_change']],
    ['Allow', 'role:owner', ['view', 'add', 'edit', 'manage', 'state_change']],
    ]
