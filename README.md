# Fasal
# Krishna Movie Application (https://krishnamantena.pythonanywhere.com/)

#  OMDB API
The OMDB API (Open Movie Database API) is an online service that provides access to a large collection of movie-related data. This includes information such as movie titles, release years, genres, directors, plot summaries, and more. The data is sourced from various contributors and is made available through an easy-to-use HTTP-based API.

## Home
The home page is the starting point of the application. From here, you can either sign up as a new user or log in if you already have an account.

## Signup
If you are a new user, select the signup option and enter your details.

![Signup](https://github.com/krishnamantena/fasal/assets/110173293/5a8df8ff-0d1b-4376-9a98-e38f232de331)

Once registered, you will be redirected to the login page.

## Login
If you already have an account, select the login option, enter your credentials, and log in.

![Login](https://github.com/krishnamantena/fasal/assets/110173293/a650d622-3d7d-4040-bc9d-72736e39d9f4)

## Main Home
After logging in, you will be redirected to the main home page.

![Main Home](https://github.com/krishnamantena/fasal/assets/110173293/4955ed1b-8514-4f8f-a5ac-dd89b4ee46bd)

Here you can find various options on the navbar, including Search, Playlist, Create Playlist, Public Playlists, and Contact.

### 1. Search
On the search page, you can search for any movie you want and add it to your playlist.

![Search](https://github.com/krishnamantena/fasal/assets/110173293/4e366862-7ac4-4d1f-8dfa-572428726586)

The code for search functionality view.py 



    def search_movies(request):
        query = request.GET.get('q')
        page_number = request.GET.get('page', 1)
        if query:
            response = requests.get(f"http://www.omdbapi.com/?apikey={API_KEY}&s={query}&page={page_number}&type=movie")
            data = response.json()
            movies = data.get('Search', [])
            total_results = int(data.get('totalResults', 0))
            paginator = Paginator(movies, 10)  # Show 10 movies per page
            page_obj = paginator.get_page(page_number)
    
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'movies': list(page_obj),
                    'currentPage': page_obj.number,
                    'totalPages': paginator.num_pages
                })
            else:
                return render(request, 'search.html', {'movies': movies, 'query': query, 'page_obj': page_obj})
        return render(request, 'search.html')


### 2. Playlist
This section displays playlists created by you.

![Playlist](https://github.com/krishnamantena/fasal/assets/110173293/24dc8b8d-622e-4f13-a1a6-02138851dbc4)


    @login_required
    def get_playlists(request):
        playlists = Playlist.objects.filter(user=request.user)
        playlist_data = [{"id": playlist.id, "name": playlist.name} for playlist in playlists]
        return JsonResponse(playlist_data, safe=False)
This function returns the list of playlist the user created. 

![Playlist](https://github.com/Ajaswanthkiran/krishna_movie/assets/91722567/023be6b5-191c-49a2-8f74-2960fac8731b)

    @login_required
    def my_playlists(request):
        playlists = Playlist.objects.filter(user=request.user)
        return render(request, 'playlists.html', {'playlists': playlists})
This function return the movies present in the playlist.


### 3. Create Playlist
In this section, you can create a new playlist. There is an option to make the playlist public. If you select the public option, the playlist will be visible to all users. If the public option is not selected, the playlist will be added to your personal playlist.

![Create Playlist](https://github.com/krishnamantena/fasal/assets/110173293/8dbd2569-9b3e-4409-91e1-24a5a791291b)

    @login_required
    def create_playlist(request):
        if request.method == 'POST':
            name = request.POST['name']
            is_public = request.POST.get('is_public') == 'on'
            playlist = Playlist.objects.create(name=name, user=request.user, is_public=is_public)
            return redirect('playlist_list')
        return render(request, 'create_playlist.html')

This function used for creating a public are private playlist.

### 4. Public Playlist
Here you can view all playlists created by any user using the public playlist option. It also shows the details of the user who created the playlist and the movies in the playlist.

![Public Playlist](https://github.com/krishnamantena/fasal/assets/110173293/b66e9e5d-87c7-46b0-92a1-d26941ff6a59)

    @login_required
    def public_playlists(request):
        public_playlists = Playlist.objects.filter(is_public=True)
        return render(request, 'public_playlists.html', {'public_playlists': public_playlists})

This function return the list of public playlist avialble from the different users and displays it.


### 5. Contact
If you encounter any issues with the application, you can contact the admin for assistance.

![Contact](https://github.com/krishnamantena/fasal/assets/110173293/59dde32d-16d7-43d0-8d4b-9012ec0df9a9)

## Conclusion
Thank you for using the Fasal application! We hope you enjoy your experience. If you have any feedback or questions, please don't hesitate to contact us through the contact section.
