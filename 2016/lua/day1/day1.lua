---Day1
---@alias Point [number, number]
local M = {}

---@enum CDIR cardinal directions.
M.CDIR = {
	N = 1,
	E = 2,
	S = 3,
	W = 4,
}

---This table is used to change direction. Simply apply -1 (left) or +1
---(right) to the index corresponding to the current orientation.
---example: Facing North then turning right:
---   dir = 'N'
---   orn = CDIR['N'] -- 1
---   new_dir = ORN[dir + 1] -- 'E'
---@type table<number, CDIR>
M.ORN = {
	[0] = M.CDIR.W,
	[1] = M.CDIR.N,
	[2] = M.CDIR.E,
	[3] = M.CDIR.S,
	[4] = M.CDIR.W,
	[5] = M.CDIR.N,
}

---@type table<string, number> convert movement direction into cardinal direction shift.
M.DIR = {
	["L"] = -1,
	["R"] = 1,
}

---Direction vectors corresponding to each cardinal direction
---@type table<CDIR, Point>
M.VEC = {
	[M.CDIR.N] = { 0, 1 },
	[M.CDIR.E] = { 1, 0 },
	[M.CDIR.S] = { 0, -1 },
	[M.CDIR.W] = { -1, 0 },
}

---Calculate the rectilinear distance between two points.
---@param p1 Point
---@param p2 Point
---@return number
function M.rectilinear_distance(p1, p2)
	local x1, y1 = p1[1], p1[2]
	local x2, y2 = p2[1], p2[2]
	return math.abs(x2 - x1) + math.abs(y2 - y1)
end

---Read a string of directions into a list.
---@param directions string
---@return string[]
function M.read_directions(directions)
	local directions_list = {}
	for dir in string.gmatch(directions, "%a%d+") do
		table.insert(directions_list, dir)
	end
	return directions_list
end

---Given a position, an orientation and a direction string, compute the new
---   position and orientation after following the direction.
---@param orientation CDIR the starting orientation.
---@param position Point the starting position.
---@param direction string the direction string to apply.
---@return [CDIR, Point] the new orientation and
---   position.
function M.follow_direction(orientation, position, direction)
	local mov, dist = string.match(direction, "(%a)(%d+)")
	local new_orientation = M.ORN[orientation + M.DIR[mov]]
	local orientation_vector = M.VEC[new_orientation]
	local movement_vector = { orientation_vector[1] * dist, orientation_vector[2] * dist }
	local new_position = { position[1] + movement_vector[1], position[2] + movement_vector[2] }
	return { new_orientation, new_position }
end

---Visit all locations between two points that share an x or a y position.
---@param start Point the starting position.
---@param finish Point the ending position.
---@return Point[]
function M.visit_locations(start, finish)
  if start[1] == finish[1] then
    local axis = 1
  else
    local axis = 2
  end

end

function M.main()
  local fh = io.open("input.txt", "r")
  local input = nil
  if fh ~= nil then
    input = fh:read()
  else
    input = ""
  end
  input = "R8, R4, R4, R8"
  local directions = M.read_directions(input)
  local orn = M.CDIR.N
  local pos = {0, 0}
  local visited = {['0,0'] = true}
  local pos_str = ""
  for _, dir in ipairs(directions) do
    local op = M.follow_direction(orn, pos, dir)
    orn, pos = op[1], op[2]
    pos_str = table.concat(pos, ",")
    print(pos_str)
    if visited[pos_str] then
      break
    end
    visited[pos_str] = true
  end
  local dist = M.rectilinear_distance({0,0}, pos)
  print(dist)
end

M.main()
