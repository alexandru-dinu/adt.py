data List a = Nil | Cons a (List a)

instance (Show a) => Show (List a) where
    show Nil = "_"
    show (Cons x xs) = (show x) ++ ":" ++ (show xs)
