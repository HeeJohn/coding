package programmers_java.hash;

// 장르별 가장 많이 재생된 노래를 두 개씩 모아서 베스트 앨범

// 수록 기준
// 1. 속한 노래가 가장 많이 재생된 장르 수록
// 2. 장르 내에서 많이 재생된 노래를 먼저 수록
// 3. 장르 내에서 재생 횟수가 같은 노래중에서는 공유 번호가 낮은 노래를 먼저 수록

//

import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.stream.Collectors;

class Genre {
    private int total;
    private List<Integer> songs;
    private String genre;

    public Genre(int total, String genre, List<Integer> songs) {
        this.total = total;
        this.genre = genre;
        this.songs = songs;
    }

    public int getTotal() {
        return this.total;
    }

    public List<Integer> getSongs() {
        return this.songs;
    }

    public String getGenre() {
        return this.genre;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    @Override
    public String toString() {

        return this.total + " " + this.genre + " " + this.songs;
    }
}

class BestAlbum {
    public List<Integer> solution(String[] genres, int[] plays) {
        HashMap<String, Genre> map = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            Genre g = map.getOrDefault(genres[i], new Genre(0, genres[i], new ArrayList()));
            g.getSongs().add(i);
            g.setTotal(g.getTotal() + plays[i]);
            map.put(genres[i], g);
        }

        List<Genre> genreList = new ArrayList<>(map.values());
        genreList.sort(Comparator.comparing(Genre::getTotal).reversed());
        for (Genre genre : genreList) {
            List<Integer> songList = genre.getSongs();
            songList.sort(Comparator.comparing((Integer i) -> plays[i]).reversed());
        }

        List<Integer> answer = genreList.stream()
                .flatMap(genre -> {
                    List<Integer> songs = genre.getSongs();

                    return songs.stream().limit(2);
                })
                .collect(Collectors.toList());


        return answer;


    }
}