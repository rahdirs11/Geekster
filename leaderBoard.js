'use strict';

function climbingLeaderBoard(ranked, player) {
	let leaderBoard = new Map();
	let rank = 1;
	for (const r of ranked) {
		console.log(`${r}:\t${leaderBoard.get(r)}`)
		leaderBoard.get(r) ?? leaderBoard.set(r, rank++)
		console.log(`Rank:\t${rank}\n\n`)
	}
	console.log(leaderBoard)
	for (const p of player) {
		console.log(`Player score:\t${p}`)
		if (p < ranked.slice(-1)) {
			ranked.push(p)
			leaderBoard.set(p, rank++)
			console.log(leaderBoard.get(p))
		} else if (ranked.includes(p)) {
			console.log(leaderBoard.get(p))
		} else if (p > ranked[0]) {
			console.log(1)
			for (const [key, value] of leaderBoard.entries()) {
				leaderBoard.set(key, value + 1)
			}
			leaderBoard.set(p, 1)
			ranked.unshift(p)
		} else {
			console.log('Work on the binary search logic')
		}
	}
}

climbingLeaderBoard([100, 90, 90, 80], [70, 80, 105])
