from voluptuous import Schema

meta_schema = Schema({
    "page": int,
    "has_next": bool,
    "has_previous": bool,
  })


course_list_schema = Schema({
        "id": int,
        "position": int,
        "title": str,
        "description": str,
        "language": str,
        "platform": int,
        "social_image_url": str,
        "courses": list,
        "similar_authors": list,
        "similar_course_lists": list,
        "similar_specializations": list,
    }
)


course_lists_schema = Schema({
        "meta": meta_schema,
        "course-lists": [course_list_schema]
})


user_schema = Schema({
    "id": int,
    "profile": str,
    "is_private": bool,
    "is_active": bool,
    "is_guest": bool,
    "is_organization": bool,
    "short_bio": str,
    "details": str,
    "first_name": str,
    "last_name": str,
    "full_name": str,
    "alias": str,
    "avatar": str,
    "cover": str,
    "city": str,
    "knowledge": int,
    "knowledge_rank": int,
    "reputation": int,
    "reputation_rank": int,
    "join_date": str,
    "social_profiles": list,
    "solved_steps_count": int,
    "created_courses_count": int,
    "created_lessons_count": int,
    "issued_certificates_count": int,
    "followers_count": int
})


profile_schema = Schema({
        "meta": meta_schema,
        "users": [user_schema]
})
