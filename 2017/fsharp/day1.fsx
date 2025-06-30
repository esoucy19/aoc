let getInput () = System.IO.File.ReadLines "./day1.txt" |> Seq.head

let stringToIntSeq (s: string) : int seq =
    s
    |> seq
    |> Seq.map (string >> System.Int32.Parse)

let cycleHead (sq: 'a seq) : 'a seq = Seq.append sq [(Seq.head sq)]

let prepareString = stringToIntSeq

let stepwise stepfn sq =
    let len = Seq.length sq
    let step = stepfn sq
    let getSnd i = Seq.item ((i + step) % len) sq
    let makePair i x = (x, getSnd i)
    sq
    |> Seq.mapi makePair

let pairwise = stepwise (fun sq -> 1)

let countIfEqualPair (a, b) =
    if a = b then a
    else 0

let captcha pairFn intSeq =
    intSeq
    |> pairFn
    |> Seq.map countIfEqualPair
    |> Seq.sum

let captcha1 = captcha pairwise

let part1 = getInput >> prepareString >> captcha1

printfn "%d" (part1 ())

let halfwaywise = stepwise (fun sq -> (Seq.length sq) / 2)

let captcha2 = captcha halfwaywise

let part2 = getInput >> prepareString >> captcha2

printfn "%d" (part2 ())