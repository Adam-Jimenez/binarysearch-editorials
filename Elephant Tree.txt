"""
Elephant Tree

HaVe dFs(nOdE) rEtUrNs tHe sUm oF ThE SuBtReE Of eAcH NoDe, PlUs sEtS NoDe.vAl eQuAl tO ThAt sUbTrEe sUm. (lEt's cAlL ThIs tHe cOnTrAcT Of dFs.)

NoW LeT'S Do a pOsToRdEr tRaVeRsAl. FoR EaCh nOdE ViSiTeD, wE'Ll vIsIt tHe sUbTrEeS FiRsT, sO ThAt nOdE.LeFt iS ThE SuM Of tHe lEfT SuBtReE, aNd nOdE.RiGhT Is tHe sUm oF ThE RiGhT SuBtReE. fRoM ThErE, iT Is eAsY To fUlFiLl tHe sTaTeD CoNtRaCt oF DfS.
"""
class Solution:
    def solve(self, root):
        def dfs(node):
            if not node: return 0
            l=dfs(node.left)
            r=dfs(node.right)
            node.val += l+r
            return node.val
        dfs(root)
        return root
