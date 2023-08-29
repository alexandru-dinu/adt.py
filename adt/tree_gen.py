def gen_tree():
    decorator_list = (
        [
            ast.Call(
                func=ast.Name(id="ADT", ctx=ast.Load()),
                args=[],
                keywords=[
                    ast.keyword(
                        arg="namespace",
                        value=ast.Call(
                            func=ast.Name(id="globals", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                    )
                ],
            )
        ],
    )

    tree = ast.ClassDef(
        name="List",
        bases=[],
        keywords=[],
        body=[
            ast.AnnAssign(
                target=ast.Name(id="Null", ctx=ast.Store()),
                annotation=ast.List(elts=[], ctx=ast.Load()),
                simple=1,
            ),
            ast.AnnAssign(
                target=ast.Name(id="Cons", ctx=ast.Store()),
                annotation=ast.List(
                    elts=[
                        ast.Tuple(
                            elts=[
                                ast.Constant(value="x"),
                                ast.Name(id="Any", ctx=ast.Load()),
                            ],
                            ctx=ast.Load(),
                        ),
                        ast.Tuple(
                            elts=[ast.Constant(value="xs"), ast.Constant(value="List")],
                            ctx=ast.Load(),
                        ),
                    ],
                    ctx=ast.Load(),
                ),
                simple=1,
            ),
        ],
        decorator_list=decorator_list,
    )

    code = ast.unparse(tree)
    return code
