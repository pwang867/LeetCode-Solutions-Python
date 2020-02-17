# edge case: such as merge ["a b", "b c"] and merge ['a', "a b c"]
class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        phrases.sort()
        head = {}
        first_words = []
        last_words = []
        for i, phrase in enumerate(phrases):
            words = phrase.split()
            first_word = words[0]
            last_word = words[-1]
            first_words.append(first_word)
            last_words.append(last_word)
            if first_word not in head:
                head[first_word] = []
            head[first_word].append(i)
        res = set()   # have to use set
        for i in range(len(phrases)):
            if i > 0 and phrases[i] == phrases[i-1]:   # skip duplicates, but can not skip all duplicates
                continue
            last_word = last_words[i]
            idx = head.get(last_word, [])
            for j in idx:
                if j == i:
                    continue
                res.add(phrases[i] + phrases[j][len(last_word):])
        return sorted(list(res))   
    
if __name__ == "__main__":
    phrases = ["elnafsbb q k as elsa s nj zohu bvtyqsif sslanu auztaj gijtw znfi igfjclnn ohuk b xwaeyo yn","fsoggiun znfi wqeh utubv c tauhgi jqxm u qb sar sh dnryb","tauhgi sh emgokxqq yn sar fy l de","ohuk","tauhgi rrdlwwu zvmq ylcpzhhc zvoq znfi yn rlftwz u wrbjzpno","de znfi wrbjzpno nj fw rrdlwwu l sziskzq jcq sslanu tauhgi w x nuwwd b m","s rlftwz svr q sar zvoq ylmbku rds b iijrqjgq vgyja nj dccbuy iijrqjgq chicvvn zvoq fw s","dccbuy dnryb m ss ys b","elsa ysaln sar hvqnpc do chicvvn","auztaj ys zvoq utubv","jrw ylmbku jrw sslanu","c w ss funhr fw rds tntqzfo nj","de","nuwwd","vkyzh rrdlwwu rlftwz b ylmbku asx b","yn chicvvn u k s","brf zohu","emgokxqq yn as afcztpgf sahqp u utubv k","sar gijtw u rds ys btmiuwh sar ylcpzhhc hvqnpc dhcf jcq fw yn vuao pooyn s","qb ylmbku eorljtgx elsa hef asx tntqzfo vgyja nj b zvmq zvoq u u","x ys vgyja rrdlwwu sslanu do fsoggiun b rrdlwwu nuwwd ul","fy s u auztaj","bvtyqsif lnkquudx b weyqrt","emgokxqq wrbjzpno rds pooyn xwaeyo sh hef pooyn nj","dhcf sziskzq btmiuwh yn wrbjzpno hvqnpc","ylmbku vkyzh w jrw","eorljtgx de c kmcm sahqp ymb h sslanu afcztpgf de","btmiuwh ylmbku zajtj chicvvn qb vkyzh l asx eorljtgx auztaj rds rds","vgyja sziskzq wqeh q","dnryb b weyqrt b fw vkyzh qb rrdlwwu xwaeyo ss hvqnpc h u","fw hvqnpc b w elsa ys s sh funhr wrbjzpno vkyzh as yn","de jrw x hef wrbjzpno ztqidl vuao hef brf hkwtvao ys dccbuy","utubv bvtyqsif fy zajtj ul fsoggiun dhcf ys hvqnpc jwlmw sh k","c fw dnryb m jcq dnryb xwaeyo afcztpgf yn zajtj hef hut auztaj rlftwz xwaeyo ss ss","zajtj jqxm zohu fsoggiun vkyzh l as c funhr sahqp k btmiuwh c","elnafsbb utubv znfi fsoggiun weyqrt auztaj ysaln rlftwz utubv sar auztaj","sar svr dhcf asx fw pooyn ztqidl l eorljtgx h znfi rrdlwwu jqxm","chicvvn fy yn hut ul rrbogif hkwtvao m asx hvqnpc ylmbku","dhcf q asx elnafsbb do l b ztqidl lnkquudx ys rrdlwwu s","btmiuwh l s qb eorljtgx l ymb fy ys jrw elnafsbb afcztpgf znfi","l nj sziskzq vgyja dnryb q utubv hut jwjbj chicvvn ss sh","aqtlwdrg","zajtj hef","as dnryb weyqrt xwaeyo","fw elnafsbb auztaj yjm lnkquudx zohu hef b ylcpzhhc chicvvn jrw yn btmiuwh q ylmbku c de","xwaeyo auztaj zajtj rlftwz pooyn aqtlwdrg afcztpgf kmcm sslanu k dhcf de s fy jwjbj u","l jcq igfjclnn vuao elsa asx znfi q rlftwz fy jrw sslanu sh hef ohuk utubv ul","ymb","iijrqjgq","ul hkwtvao hkwtvao hef aqtlwdrg nj","hvqnpc jrw ss brf kbibako hkwtvao pooyn aqtlwdrg tauhgi ohuk sziskzq jcq","h fy eorljtgx xwaeyo zohu gijtw sh zvmq elsa jwjbj jwjbj ysaln l","tntqzfo ylcpzhhc b jwlmw gijtw ys auztaj q nj fy de ymb fw fw","ohuk","weyqrt tauhgi chicvvn ymb wrbjzpno vgyja btmiuwh","sh zohu funhr qb ys wqeh h yn c","nuoqfc","nj sslanu zvmq h q","jwjbj vuao fw fy aqtlwdrg sahqp pooyn elnafsbb fw svr q ul ztqidl hkwtvao rlftwz","jwjbj ysaln k l wrbjzpno yn utubv dnryb de k pooyn tauhgi yjm","funhr rrdlwwu m","sahqp aqtlwdrg b yn c ymb","rrbogif ylmbku vkyzh ylmbku rlftwz aqtlwdrg hut","vuao zajtj dhcf wrbjzpno jcq tntqzfo ohuk ss emgokxqq bvtyqsif jqxm igfjclnn wqeh l elnafsbb","elsa u elnafsbb igfjclnn dccbuy hkwtvao","dhcf dhcf rrbogif as do jwlmw l nj jwlmw vkyzh svr","m q x vgyja sahqp m xwaeyo do pooyn xwaeyo ohuk","b","l yjm vkyzh rds sslanu gijtw l zajtj sar m","ss aqtlwdrg rlftwz dccbuy zohu do elsa ylcpzhhc hkwtvao tntqzfo k u jwjbj rlftwz l w","s wrbjzpno ul iijrqjgq ss s svr nuwwd xwaeyo tauhgi znfi btmiuwh sh yn jwjbj qb znfi","yn","pooyn pooyn","kbibako x ss jrw de aqtlwdrg zohu ss","b hkwtvao rds ymb sziskzq w ysaln zvmq kmcm nuoqfc fw nj q qb","znfi vgyja tntqzfo ylcpzhhc ul ymb","funhr sh kmcm","rds dhcf btmiuwh l btmiuwh x eorljtgx q as zajtj emgokxqq q ylmbku","jqxm ztqidl igfjclnn lnkquudx auztaj jrw weyqrt hut nuwwd elsa xwaeyo l","jrw elsa igfjclnn vuao qb auztaj ztqidl zohu vkyzh aqtlwdrg bvtyqsif funhr hkwtvao","fsoggiun weyqrt brf jwlmw jwlmw utubv do do l svr","vkyzh tntqzfo ysaln aqtlwdrg ys dccbuy lnkquudx btmiuwh nuoqfc gijtw ul kmcm vuao","nj ysaln hut ylmbku svr igfjclnn vkyzh yn x jwlmw ohuk w","hef c kmcm zvmq fsoggiun gijtw m","xwaeyo jwjbj vgyja vkyzh rrbogif zohu btmiuwh m tntqzfo ohuk nuoqfc asx w jrw m","as tntqzfo tauhgi dnryb jcq rrdlwwu iijrqjgq brf l jcq","yn l jqxm l eorljtgx rrdlwwu yjm u","lnkquudx auztaj zajtj hut b m ysaln jwjbj","b h hvqnpc asx vgyja","jrw zohu rds c zvmq ymb asx zvoq dhcf sar aqtlwdrg vkyzh yjm rds ul ss wqeh"]
    print(Solution().beforeAndAfterPuzzles(phrases))

"""
Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.

 

Example 1:

Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]
Example 2:

Input: phrases = ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
Output: ["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"]
Example 3:

Input: phrases = ["a","b","a"]
Output: ["a"]
"""
