# global
from hypothesis import strategies as st, settings

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers.testing_helpers import handle_frontend_test


# can_cast
@handle_frontend_test(
    fn_tree="jax.numpy.can_cast",
    from_=helpers.get_dtypes("valid", full=False),
    to=helpers.get_dtypes("valid", full=False),
    casting=st.sampled_from(["no", "equiv", "safe", "same_kind", "unsafe"]),
    test_with_out=st.just(False),
)
# there are 100 combinations of dtypes, so run 200 examples to make sure all are tested
@settings(max_examples=200)
def test_jax_numpy_can_cast(
    *,
    from_,
    to,
    casting,
    test_flags,
    on_device,
    fn_tree,
    frontend,
    backend_fw,
):
    helpers.test_frontend_function(
        input_dtypes=[],
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        from_=from_[0],
        to=to[0],
        casting=casting,
    )


# promote_types
@handle_frontend_test(
    fn_tree="jax.numpy.promote_types",
    type1=helpers.get_dtypes("valid", full=False),
    type2=helpers.get_dtypes("valid", full=False),
    test_with_out=st.just(False),
)
# there are 100 combinations of dtypes, so run 200 examples to make sure all are tested
@settings(max_examples=200)
def test_jax_numpy_promote_types(
    *,
    type1,
    type2,
    test_flags,
    on_device,
    fn_tree,
    frontend,
    backend_fw,
):
    ret, frontend_ret = helpers.test_frontend_function(
        input_dtypes=[],
        backend_to_test=backend_fw,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        type1=type1[0],
        type2=type2[0],
        test_values=False,
    )
    assert str(ret._ivy_dtype) == frontend_ret[0].name
