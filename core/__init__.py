"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/mukund123456>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from core.song import Song
from core.groups import (
    get_group, get_queue, set_group, set_title, all_groups, clear_queue,
    set_default, shuffle_queue)
from core.funcs import (
    app, ydl, safone, search, restart, pytgcalls, skip_stream, check_yt_url,
    extract_args, start_stream, generate_cover, delete_messages,
    get_youtube_playlist)
